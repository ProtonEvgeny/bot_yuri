# -*- coding: utf-8 -*-
import scrapy

class yuri_spider(scrapy.Spider):
    name = 'visibility_google'
    
    def start_requests(self):
        urls = [
            f'https://a.pr-cy.ru/{self.URL}/',
        ]
        cookie = [
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1698945071.238552,
            "hostOnly": False,
            "httpOnly": True,
            "name": "__ddg1_",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "w7ycNXBaHAzSbZDRXT2j",
            "id": 1
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1701972212.38293,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ga",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "GA1.1.1031966977.1667409072",
            "id": 2
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1701972272.287989,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ga_5BLD66Z49D",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "GS1.1.1667409072.1.1.1667412272.54.0.0",
            "id": 3
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667498612,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_gid",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "GA1.2.1606439584.1667409072",
            "id": 4
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667414043,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_hjAbsoluteSessionInProgress",
            "path": "/",
            "sameSite": "lax",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "0",
            "id": 5
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667414043,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_hjFirstSeen",
            "path": "/",
            "sameSite": "lax",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "1",
            "id": 6
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667414043,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_hjSession_1395883",
            "path": "/",
            "sameSite": "lax",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "eyJpZCI6ImFlODM2OWJlLWJmNTQtNDY4OC1iODZkLWY4YmVhYjJiYzhhNCIsImNyZWF0ZWQiOjE2Njc0MTIyMTI5MjQsImluU2FtcGxlIjpmYWxzZX0=",
            "id": 7
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1698948212,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_hjSessionUser_1395883",
            "path": "/",
            "sameSite": "lax",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "eyJpZCI6ImEzYWE4OTU5LWI0MDYtNTU0My1hY2RkLWE2NTI5NTQzMWZmYSIsImNyZWF0ZWQiOjE2Njc0MTIyMTI3MTEsImV4aXN0aW5nIjpmYWxzZX0=",
            "id": 8
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1698945072,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ym_d",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "1667409073",
            "id": 9
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667499034,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ym_hostIndex",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "0-6%2C1-5",
            "id": 10
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667481072,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ym_isad",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "2",
            "id": 11
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1698945072,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ym_uid",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "1667409073837199761",
            "id": 12
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1667414012,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ym_visorc",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "w",
            "id": 13
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1701972212.411124,
            "hostOnly": False,
            "httpOnly": False,
            "name": "amp_28f667",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "WilFbIaYq0B5HbZv05Butc.MTA5NTE4NQ==..1ggsl6kf1.1ggso6elk.p.d.16",
            "id": 14
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1670001391.976338,
            "hostOnly": False,
            "httpOnly": False,
            "name": "balanceUpdate",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "1667409391",
            "id": 15
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1670004204.888801,
            "hostOnly": False,
            "httpOnly": True,
            "name": "cs",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "%242a%2412%243MogCdkRhI3cbR50lRXlG.x32XwZyWDhlb1jcrEyE7Jg9w06QVd2i",
            "id": 16
        },
        {
            "domain": ".pr-cy.ru",
            "hostOnly": False,
            "httpOnly": True,
            "name": "PHPSESSID",
            "path": "/",
            "sameSite": "unspecified",
            "secure": True,
            "session": True,
            "storeId": "0",
            "value": "f46f9f1e3e77988e0111aa69f67bbe9d",
            "id": 17
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1670004204.888832,
            "hostOnly": False,
            "httpOnly": False,
            "name": "profileUpdate",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "1656589209",
            "id": 18
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1670004204.88876,
            "hostOnly": False,
            "httpOnly": True,
            "name": "uhash",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "%242a%2412%24GJtwP07wYLaBNigNPOrPUOggdFHnRo4eI0%2FlAIJF8vmycS7QFsyiK",
            "id": 19
        },
        {
            "domain": ".pr-cy.ru",
            "expirationDate": 1670004204.888667,
            "hostOnly": False,
            "httpOnly": True,
            "name": "uid",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "1095185",
            "id": 20
        }
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookie)

    
    def parse(self, response):
      for i in range(2, 12):
        yield {
            'Ключевое слово' : response.xpath(f'//*[@id="app"]/div[3]/div[4]/div[6]/div/div[5]/div/div/div/div/div/div/div/table/tbody/tr[{i}]/td[1]/text()').get(),
            'Позиция' : response.xpath(f'//*[@id="app"]/div[3]/div[4]/div[6]/div/div[5]/div/div/div/div/div/div/div/table/tbody/tr[{i}]/td[2]/text()').get(),
            'Показов' : response.xpath(f'//*[@id="app"]/div[3]/div[4]/div[6]/div/div[5]/div/div/div/div/div/div/div/table/tbody/tr[{i}]/td[3]/text()').get().replace('&nbsp;', ' '),
            'URL' : response.xpath(f'//*[@id="app"]/div[3]/div[4]/div[6]/div/div[5]/div/div/div/div/div/div/div/table/tbody/tr[{i}]/td[4]/a/text()').get()
        }
