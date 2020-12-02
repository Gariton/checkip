#!/usr/bin/env python3
# main.py : 1.セッション貼り直し自動検知及びDNS自動更新
#           2.DNS改ざん検知

import checkIp
import linenotify
import ddns

if __name__ == "__main__":
  #1.セッション貼り直し検知及びDNS自動更新
  ip_result = checkIp.difference()
  if ip_result:
    #変動あり
    print("[セッション貼り直し]")
    #Line通知送信
    print("Line通知送信中...")
    ln1 = linenotify.send("\n自宅のセッション貼り直しが検知されました。\n IP:" + ip_result)
    if ln1:
      print("送信完了")
    else:
      print("送信失敗")

    #DNS自動更新
    print("[DNS更新]")
    ddns.updateip(ip_result)
    print("Line通知送信中...")
    ln2 = linenotify.send("\n下記ドメインのDNS設定をしました。\n Domain:" + ddns.domname + "\n IP:" + ip_result)
    if ln2:
      print("送信完了")
    else:
      print("送信失敗")

  #2.DNS改ざん検知
  #dns_result = ddns.checkDns()
  #if dns_result:
  #  #DNS更新検知
  #  print("[DNS改ざん検知]")
  #  ln3 = linenotify.send("\nDNS更新を検知しました。\n IP:" + dns_result)
  #  if ln3:
  #    print("送信完了")
  #  else:
  #    print("送信失敗")

