import re
import requests
import logging
from collections import defaultdict, OrderedDict
from datetime import datetime
import config

# 配置日志记录
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler("function.log", "w", encoding="utf-8"), 
                              logging.StreamHandler()])

# 解析模板文件，获取频道分类及其对应的频道列表
def parse_template(template_file):
    template_channels = defaultdict(list)
    current_category = None

    with open(template_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if "#genre#" in line:
                    current_category = line.split(",")[0].strip()
                elif current_category:
                    channel_name = line.split(",")[0].strip()
                    template_channels[current_category].append(channel_name)

    return template_channels

# 从指定URL中获取频道及其直播源链接
def fetch_channels(url):
    channels = defaultdict(list)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        lines = response.text.splitlines()

        current_category = None
        is_m3u = any("#EXTINF" in line for line in lines[:15])
        logging.info(f"url: {url} 获取成功，判断为{'m3u' if is_m3u else 'txt'}格式")

        if is_m3u:
            for line in lines:
                line = line.strip()
                if line.startswith("#EXTINF"):
                    match = re.search(r'group-title="(.*?)",(.*)', line)
                    if match:
                        current_category = match.group(1).strip()
                        channel_name = match.group(2).strip()
                elif line and not line.startswith("#"):
                    channel_url = line.strip()
                    if current_category and channel_name:
                        channels[current_category].append((channel_name, channel_url))
        else:
            for line in lines:
                line = line.strip()
                if "#genre#" in line:
                    current_category = line.split(",")[0].strip()
                elif current_category:
                    match = re.match(r"^(.*?),(.*?)$", line)
                    if match:
                        channel_name = match.group(1).strip()
                        channel_url = match.group(2).strip()
                        channels[current_category].append((channel_name, channel_url))
                    elif line:
                        channels[current_category].append((line, ''))

        if channels:
            categories = ", ".join(channels.keys())
            logging.info(f"url: {url} 爬取成功✅，包含频道分类: {categories}")
    except requests.RequestException as e:
        logging.error(f"url: {url} 爬取失败❌, Error: {e}")

    return channels    

# 匹配模板中的频道和抓取到的频道
def match_channels(template_channels, all_channels):
    matched_channels = defaultdict(list)

    for category, channels in template_channels.items():
        if category in all_channels:
            for template_channel in channels:
                for channel_name, channel_url in all_channels[category]:
                    if template_channel.lower() in channel_name.lower():
                        matched_channels[category].append((channel_name, channel_url))

    return matched_channels

# 从所有配置的源抓取频道并匹配模板中的频道
def filter_source_urls(template_file):
    template_channels = parse_template(template_file)
    source_urls = config.source_urls

    all_channels = defaultdict(list)
    for url in source_urls:
        fetched_channels = fetch_channels(url)
        for category, channel_list in fetched_channels.items():
            all_channels[category].extend(channel_list)

    matched_channels = match_channels(template_channels, all_channels)

    return matched_channels, template_channels

# 将匹配的频道写入M3U和TXT文件
def updateChannelUrlsM3U(channels, template_channels):
    written_urls = set()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 写入M3U文件
    with open("live.m3u", "w", encoding="utf-8") as f_m3u:
        f_m3u.write(f"#EXTM3U x-tvg-url={','.join(f'\"{epg_url}\"' for epg_url in config.epg_urls)}\n")

        for category, channel_list in channels.items():
            for channel_name, channel_url in channel_list:
                if channel_url and channel_url not in written_urls:
                    f_m3u.write(f"#EXTINF:-1 group-title=\"{category}\",{channel_name}\n{channel_url}\n")
                    written_urls.add(channel_url)

    # 写入TXT文件
    with open("live.txt", "w", encoding="utf-8") as f_txt:
        f_txt.write(f"Updated: {current_date}\n")
        for category, channel_list in channels.items():
            f_txt.write(f"#genre# {category}\n")
            for channel_name, channel_url in channel_list:
                f_txt.write(f"{channel_name},{channel_url}\n")

# 主执行逻辑
if __name__ == "__main__":
    template_file = "demo.txt"
    channels, template_channels = filter_source_urls(template_file)
    updateChannelUrlsM3U(channels, template_channels)
