取之于民，用之于民

关于这个库的作用：主要用来将已经测试有效的直播源进行分类整理、标记直播源类型IPV6%IPV4！！！满足适合自己的使用习惯！！

直播源是否有效需要配合：https://github.com/Guovin/TV，先测试。也可以直接使用这个库达到目的，但不能标记类型。

自定义使用，修改示例：

1、修改频道：

修改demo.txt，如：央视,#genre#

                  CCTV1, 
                  
                  CCTV2,
                  
                  CCTV3,
                  
                  .........，
                  
                  卫视,#genre#
                  
                  湖南卫视,
                  
                  浙江卫视,
                  
                  东方卫视,
                  
                  .........,

                  
2、修改IPV6与IPV4排列顺序：

修改main.py，其中的IPV6和IPV4可以修改，直播源数量20个可以修改，如：

                            # 提取前20个IPv6和前20个IPv4的直播源
                            ipv6_streams = [url for url in filtered_urls if is_ipv6(url)][:20]
                            ipv4_streams = [url for url in filtered_urls if not is_ipv6(url)][:20]

                            # 将IPv6放在前面，IPv4放在后面
                            combined_streams = ipv6_streams + ipv4_streams

                            total_urls = len(combined_streams)
                            for index, url in enumerate(combined_streams, start=1):
                                if is_ipv6(url):
                                    url_suffix = f"$IPV6" if total_urls == 1 else f"$IPV6『线路{index}』"
                                else:
                                    url_suffix = f"$IPV4" if total_urls == 1 else f"$IPV4『线路{index}』"
                                base_url = url.split('$', 1)[0] if '$' in url else url
                                new_url = f"{base_url}{url_suffix}"


3、修改扫源订阅地址：

注意：逗号为英文逗号，中文逗号会导致运行错误！！！！

注意：逗号为英文逗号，中文逗号会导致运行错误！！！！

注意：逗号为英文逗号，中文逗号会导致运行错误！！！！

修改config.py，其中source_urls = 下的网址是扫源的订阅地址，如：

source_urls = [

    "https://m3u.hackserver.net/txt/fmml_ipv6.txt",
    
    "https://m3u.hackserver.net/txt/fmml_dv6.txt",
    
    "https://raw.githubusercontent.com/YueChan/Live/main/APTV.m3u",
    
    "https://m3u.hackserver.net/txt/y_g.txt",
    
    "https://m3u.hackserver.net/txt/j_iptv.txt",




    关于如何在GitHub上自动运行：
    请参考开启 Actions 工作流：  https://github.com/Guovin/TV/blob/master/docs/tutorial.md
