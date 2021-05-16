# week day5

**Mission 1**의 API 명세서입니다.

\
**GET**

/whoami GET

http://127.0.0.1:5000/whoami

`github id`를 반환받기 위한 쿼리

\
**Example Request**

/whoami GET

``` {.click-to-expand-wrapper .is-snippet-wrapper .language-javascript data-title="Example Request" data-content-type="example-request" data-id="51e27b7a-0fe8-43b6-a0e2-b29a33882dfd_0" data-clipboard-target="#http_0_51e27b7a-0fe8-43b6-a0e2-b29a33882dfd" data-before-copy="Copy to Clipboard" data-after-copy="Copied"}
GET /whoami HTTP/1.1
Host: 127.0.0.1:5000
```

\
**GET**

/echo GET

http://127.0.0.1:5000/echo?string=this is SW

string=`string`\
`string`을 echo해주는 쿼리

Example String : `this is SW`

\
**Example Request**

/echo GET

``` {.click-to-expand-wrapper .is-snippet-wrapper data-title="Example Request" data-content-type="example-request" data-id="288f72fe-d3c6-4ee0-a780-2c1894a20286_0" data-clipboard-target="#http_0_288f72fe-d3c6-4ee0-a780-2c1894a20286" data-before-copy="Copy to Clipboard" data-after-copy="Copied"}
GET /echo?string=this is SW HTTP/1.1
Host: 127.0.0.1:5000
```
* * * * *

\
**GET**

/weapons GET

http://127.0.0.1:5000/weapons

보유 무기 현황을 반환하는 쿼리

\
**Example Request**

/weapons GET

``` {.click-to-expand-wrapper .is-snippet-wrapper data-title="Example Request" data-content-type="example-request" data-id="f67411c9-9bc0-43d0-90a5-f9cc8bb94d53_0" data-clipboard-target="#http_0_f67411c9-9bc0-43d0-90a5-f9cc8bb94d53" data-before-copy="Copy to Clipboard" data-after-copy="Copied"}
GET /weapons HTTP/1.1
Host: 127.0.0.1:5000
```

\
**POST**

/weapons POST

http://127.0.0.1:5000/weapons

새로운 무기를 추가하기 위한 쿼리

**BODY raw**

``` {.body-block .click-to-expand-wrapper .is-snippet-wrapper data-title="BODY Raw" data-id="908c954d-0367-4e67-8c3e-c3ecf3dfa0a0"}
{
    "name" : "pen",
    "stock" : 10000
}
```

\
**Example Request**

/weapons POST

``` {.click-to-expand-wrapper .is-snippet-wrapper data-title="Example Request" data-content-type="example-request" data-id="908c954d-0367-4e67-8c3e-c3ecf3dfa0a0_0" data-clipboard-target="#http_0_908c954d-0367-4e67-8c3e-c3ecf3dfa0a0" data-before-copy="Copy to Clipboard" data-after-copy="Copied"}
POST /weapons HTTP/1.1
Host: 127.0.0.1:5000
Content-Length: 46

{
    "name" : "pen",
    "stock" : 10000
}
```

\
**PUT**

/weapons PUT

http://127.0.0.1:5000/weapons

기존의 무기 상태를 갱신하기 위한 쿼리

**BODY raw**

``` {.body-block .click-to-expand-wrapper .is-snippet-wrapper data-title="BODY Raw" data-id="ff476f1e-1258-4034-a50b-99fc3f44e0bf"}
{
    "name" : "pen",
    "stock" : 20000
}
```

\
**Example Request**

/weapons PUT

``` {.click-to-expand-wrapper .is-snippet-wrapper data-title="Example Request" data-content-type="example-request" data-id="ff476f1e-1258-4034-a50b-99fc3f44e0bf_0" data-clipboard-target="#http_0_ff476f1e-1258-4034-a50b-99fc3f44e0bf" data-before-copy="Copy to Clipboard" data-after-copy="Copied"}
PUT /weapons HTTP/1.1
Host: 127.0.0.1:5000
Content-Length: 46

{
    "name" : "pen",
    "stock" : 20000
}
```

\
**DEL**

/weapons DELETE

http://127.0.0.1:5000/weapons/pen

무기를 폐기하기 위한 쿼리

\
**Example Request**

/weapons DELETE

``` {.click-to-expand-wrapper .is-snippet-wrapper data-title="Example Request" data-content-type="example-request" data-id="bf57ec12-1d16-4d2a-94df-6870693f0d7e_0" data-clipboard-target="#http_0_bf57ec12-1d16-4d2a-94df-6870693f0d7e" data-before-copy="Copy to Clipboard" data-after-copy="Copied"}
DELETE /weapons/pen HTTP/1.1
Host: 127.0.0.1:5000
```