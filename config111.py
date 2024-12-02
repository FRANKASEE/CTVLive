ip_version_priority = "ipv6"

source_urls = [
    "https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    "https://raw.githubusercontent.com/frank11311/TV/refs/heads/master/result.txt",
    "https://raw.githubusercontent.com/FRANKASEE/TV/refs/heads/master/result.txt",
    "https://raw.githubusercontent.com/FRANKASEE/tvk/refs/heads/main/cctv.txt",
    "https://raw.githubusercontent.com/FRANKASEE/tvk/refs/heads/main/weishi.txt",
    "https://raw.githubusercontent.com/FRANKASEE/tviptv/refs/heads/Files/CNTV.m3u",
    "https://raw.githubusercontent.com/FRANKASEE/tviptv/refs/heads/Files/CCTV.m3u",
    "https://raw.githubusercontent.com/suxuang/myIPTV/refs/heads/main/ipv6.m3u",
]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn"
]

announcements = [
    {
        "channel": "定制直播",
        "entries": [
            {"name": "影视直播", "url": "https://cors.isteed.cc", "logo": "https://cors.isteed.cc"},
            {"name": "CrimeTV LIVE", "url": "https://cors.isteed.cc", "logo": "https://cors.isteed.cc"},
            {"name": "更新日期", "url": "https://cors.isteed.cc", "logo": "https://cors.isteed.cc"},
            {"name": None, "url": "https://cors.isteed.cc", "logo": "https://cors.isteed.cc"}
        ]
    }
]

epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
