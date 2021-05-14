# bicsubi_extra_api

This is a simple API

## Version: 1.0.0

**Contact information:**  
you@your-company.com  

**License:** [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

### /weather

#### GET
##### Summary:

날씨를 알 수 있는 API

##### Description:

현재 위치의 위도와 경도 값을 이용해 현재 위치의 날씨(온도, 바람세기 등)을 알 수 있는 API

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| Location | body | 현재 위치 | No | [Location](#Location) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [ [Weather](#Weather) ] |
| 400 | Fail |  |

### /bus

#### GET
##### Summary:

버스 정류장의 도착정보 API

##### Description:

현재 위치의 위도와 경도 값을 이용해 현재 위치에서 가장 가까운 버스 정류장의 도착정보를 알 수 있는 API

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| Location | body | 현재 위치 | No | [Location](#Location) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Success | [ [BusStop](#BusStop) ] |
| 400 | Fail |  |

### Models


#### Weather

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| temperature | number (float64) |  | Yes |
| windSpeed | number (float64) |  | Yes |

#### BusStop

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| name | string |  | Yes |
| busInfo | [ string ] |  | Yes |

#### Location

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| latitude | number (float64) |  | Yes |
| longitude | number (float64) |  | Yes |

## raw swagger code

```s
swagger: '2.0'
info:
  description: This is a simple API
  version: 1.0.0
  title: Simple Inventory API
  # put the contact info for your development or API team
  contact:
    email: you@your-company.com

  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html

# tags are used for organizing operations
tags:
- name: admins
  description: Secured Admin-only calls
- name: developers
  description: Operations available to regular developers

paths:
  /weather:
    get:
      tags:
      - 날씨
      summary: 날씨를 알 수 있는 API
      operationId: searchWeather
      description: 현재 위치의 위도와 경도 값을 이용해 현재 위치의 날씨(온도, 바람세기 등)을 알 수 있는 API
      produces:
      - application/json
      parameters:
      - in: body
        name: Location
        description: 현재 위치
        schema:
          $ref: '#/definitions/Location'
      responses:
        200:
          description: Success
          schema:
            type: array
            items:
              $ref: '#/definitions/Weather'
        400:
          description: Fail
  /bus:
    get:
      tags:
      - 버스 정류장
      summary: 버스 정류장의 도착정보 API
      operationId: searchBusStop
      description: 현재 위치의 위도와 경도 값을 이용해 현재 위치에서 가장 가까운 버스 정류장의 도착정보를 알 수 있는 API
      produces:
      - application/json
      parameters:
      - in: body
        name: Location
        description: 현재 위치
        schema:
          $ref: '#/definitions/Location'
      responses:
        200:
          description: Success
          schema:
            type: array
            items:
              $ref: '#/definitions/BusStop'
        400:
          description: Fail
definitions:
  Weather:
    required:
    - temperature
    - windSpeed
    type: object
    properties:
      temperature:
        type: number
        format: float64
        example: 25.5
      windSpeed:
        type: number
        format: float64
        example: 4.3
  BusStop:
    required:
    - name
    - busInfo
    type: object
    properties:
      name:
        type: string
        example: "서울역 앞 버스정류장"
      busInfo:
        type: array
        items:
          type: string
          example: "7"
        example: ["7", "M4353"]
  Location:
    required:
    - latitude
    - longitude
    type: object
    properties:
      latitude:
        type: number
        format: float64
        example: 35.9078
      longitude:
        type: number
        format: float64
        example: 127.7669
# Added by API Auto Mocking Plugin
host: virtserver.swaggerhub.com
basePath: /hwangwoojin/bicsubi_extra_api/1.0.0
schemes:
 - https
```
