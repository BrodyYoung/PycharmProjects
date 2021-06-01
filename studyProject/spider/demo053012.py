import json

json_str = '''[
  {
    "id": 8889479,
    "createTime": 1622338519000,
    "modifyTime": 1622338519000,
    "tags": "",
    "countryType": 2,
    "continents": "欧洲",
    "provinceId": "5",
    "provinceName": "法国",
    "provinceShortName": "",
    "cityName": "",
    "currentConfirmedCount": 5458939,
    "confirmedCount": 5921696,
    "confirmedCountRank": 4,
    "suspectedCount": 0,
    "curedCount": 353370,
    "deadCount": 109387,
    "deadCountRank": 8,
    "deadRate": "1.84",
    "deadRateRank": 80,
    "comment": "",
    "sort": 0,
    "operator": "chenlele1",
    "locationId": 961002,
    "countryShortCode": "FRA",
    "countryFullName": "France",
    "statisticsData": "https://file1.dxycdn.com/2020/0315/929/3402160538577857318-135.json",
    "incrVo": {
      "currentConfirmedIncr": 3964,
      "confirmedIncr": 4299,
      "curedIncr": 0,
      "deadIncr": 335
    },
    "showRank": true,
    "yesterdayConfirmedCount": 2147383647,
    "yesterdayLocalConfirmedCount": 2147383647,
    "yesterdayOtherConfirmedCount": 2147383647,
    "highDanger": "",
    "midDanger": "",
    "highInDesc": "",
    "lowInDesc": "",
    "outDesc": ""
  },
  {
    "id": 8889482,
    "createTime": 1622338520000,
    "modifyTime": 1622338520000,
    "tags": "",
    "countryType": 2,
    "continents": "北美洲",
    "provinceId": "8",
    "provinceName": "美国",
    "provinceShortName": "",
    "cityName": "",
    "currentConfirmedCount": 4837206,
    "confirmedCount": 33249494,
    "confirmedCountRank": 1,
    "suspectedCount": 0,
    "curedCount": 27818020,
    "deadCount": 594268,
    "deadCountRank": 1,
    "deadRate": "1.78",
    "deadRateRank": 87,
    "comment": "",
    "sort": 0,
    "operator": "chenlele1",
    "locationId": 971002,
    "countryShortCode": "USA",
    "countryFullName": "United States of America",
    "statisticsData": "https://file1.dxycdn.com/2020/0315/553/3402160512808052518-135.json",
    "incrVo": {
      "currentConfirmedIncr": -86229,
      "confirmedIncr": 30887,
      "curedIncr": 116141,
      "deadIncr": 975
    },
    "showRank": true,
    "yesterdayConfirmedCount": 2147383647,
    "yesterdayLocalConfirmedCount": 2147383647,
    "yesterdayOtherConfirmedCount": 2147383647,
    "highDanger": "",
    "midDanger": "",
    "highInDesc": "",
    "lowInDesc": "",
    "outDesc": ""
  }]'''

js = json.loads(json_str)

# python类型数据转换为json字符串
json_str = json.dumps(js, ensure_ascii=False)
print(json_str)

# python类型数据转换为json格式文件
with open('resrc/ttt.json', 'w') as fi:
    json.dump(js, fi, ensure_ascii=False)
