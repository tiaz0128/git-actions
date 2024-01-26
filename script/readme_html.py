start_html = """
 <div
      style="
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        padding: 20px;
        border: 2px solid black;
      "
    >
"""

avatar_html = """
    <avata style="position: relative">
        <span
          style="
            position: absolute;
            text-align: center;
            font-size: 12px;
            font-weight: 700;
            color: white;
            background-color: steelblue;
            padding: 4px 7px;
            border-radius: 10%;
          "
          >{cnt} / {total}</span
        >
        <div
          style="
            width: 100px;
            height: 100px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 10px;
            border: 2px solid rgba(22, 22, 22, 0.278);
            background: url('{img}');
            background-size: cover;
          "
        ></div>
        <div>
          <span style="text-align: center; font-size: 14px">{name}</span>
          <span style="text-align: center; font-size: 14px">({id})</span>
        </div>
        <a target="_blank" href="{url}"
          ><span style="text-align: center; font-size: 14px"
            >문제 풀이 보러가기</span
          ></a
        >
      </avata>
"""

end_html = """
    </div>
"""
