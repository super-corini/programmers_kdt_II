## bicsubi Weapon Data 갱신 및 삭제

1. bicsubi Data 무기 열람하는법
    - `GET /show`
    - 출력 :    {
                    "weapon_name",
                    "stock"
                }
2. bicsubi Data 무기 추가
    - `POST /<int:stock>?weapon="weapon_name"`
        - `<int:stock>`자리에 stock, `"weapon_name"`자리에 무기 이름 기입
    - 정상 작동시 `CREATE COMPLETE!` 출력

3. bicsubi Data 무기 갱신
    - `PUT /update_weapon?weapon="weapon_name"`
        - `"weapon_name"` 자리에 무기 이름
        - `{"weapon":"new_weapon_name", "stock":<int:stock>}` 입력
        - `"weapon_name"` 이 같은 곳에 new_weapon_name, stock으로 변경
    - 정상 작동시 `UPDATE COMPLETE!` 출력
    - 만약 db에 없는 무기를 갱신하려한다면 404에러 발생

4. bicsubi Data 무기 삭제
    - `DELETE /delete?weapon="weapon_name"`
        - `"weapon_name"` 자리에 무기 이름 입력
    - 만약 db에 없는 무기를 삭제하려한다면 404에러 발생

5. github id 보는법
    - `GET /whoami`
    - 출력 : 
    <pre>
    <code>
    {
        "name" : "wkdclrms123"
    }
    </code>
    </pre>

