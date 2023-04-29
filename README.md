# RelBintang
![image](https://user-images.githubusercontent.com/45286708/234468868-882684ff-82ef-452b-922d-7ca4306563ce.png)



1. Buka dan login ke [websitenya](https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&lang=en&plat_type=pc) 
2. Salin dan tempel kode ini ke browser console (klik F12) untuk mendapatkan COOKIES
 ```
var cookie = document.cookie
cookie = cookie.replaceAll(" ","")
var ask = confirm('Cookie: ' + cookie + '\n\nClick confirm to copy Cookie.'); 
if (ask == true) { 
    copy(cookie); 
    msg = cookie 
} 
else msg = 'Cancel'
```

3. Buka https://github.com/username/RelBintang/settings/secrets/actions dan klik `New repository secret`
![image](https://user-images.githubusercontent.com/45286708/234468103-12ead4c9-84cc-4e49-b78d-871fcbe358f7.png)

4. Isi `Name *` dengan `COOKIES`
5. Tempel COOKIES yang tadi disalin ke dalam `Secret *`
6. Klik `Add secret`
![image](https://user-images.githubusercontent.com/45286708/234468227-b226bbbf-030c-4ca4-ae0e-46d8c46d88d5.png)

7. Buka https://github.com/username/RelBintang/actions/workflows/main.yml
8. Klik `Run workflow`
![image](https://user-images.githubusercontent.com/45286708/234468303-61e1ce3c-f2d4-41cd-b315-8816d607e01a.png)

Untuk dua akun atau lebih format penulisan cookiesnya `["COOKIES1", "COOKIES2", ...]`
