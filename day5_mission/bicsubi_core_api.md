# bicsubi - core

Assistant of Bronze-man

## Version: 0.1.0

### /whoami

#### GET

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  | Success     |

### /echo

#### GET

##### Parameters

| Name   | Located in | Description          | Required | Schema |
| ------ | ---------- | -------------------- | -------- | ------ |
| string | query      | String to be echoed. | Yes      | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  | Success     |

### /weapon

#### POST

##### Parameters

| Name  | Located in | Description                 | Required | Schema  |
| ----- | ---------- | --------------------------- | -------- | ------- |
| name  | query      | Name of the weapon.         | Yes      | string  |
| stock | query      | Amount of weapon available. | No       | integer |

##### Responses

| Code | Description                    |
| ---- | ------------------------------ |
| 200  | Successful.                    |
| 400  | Bad request or malformed data. |
| 500  | Server error.                  |

#### DELETE

##### Parameters

| Name | Located in | Description         | Required | Schema |
| ---- | ---------- | ------------------- | -------- | ------ |
| name | query      | Name of the weapon. | Yes      | string |

##### Responses

| Code | Description                    |
| ---- | ------------------------------ |
| 200  | Successful.                    |
| 400  | Bad request or malformed data. |
| 500  | Server error.                  |

#### PUT

##### Parameters

| Name     | Located in | Description                 | Required | Schema  |
| -------- | ---------- | --------------------------- | -------- | ------- |
| name     | query      | Name of the weapon.         | Yes      | string  |
| stock    | query      | Amount of weapon available. | No       | integer |
| new_name | query      | New name of weapon.         | No       | string  |

##### Responses

| Code | Description                    |
| ---- | ------------------------------ |
| 200  | Successful.                    |
| 400  | Bad request or malformed data. |
| 500  | Server error.                  |

#### GET

##### Responses

| Code | Description                    |
| ---- | ------------------------------ |
| 200  | Successful.                    |
| 400  | Bad request or malformed data. |
| 500  | Server error.                  |