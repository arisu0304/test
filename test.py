import json
import math


if __name__== "__main__":
    with open('visits.json', 'r') as f:
        visits = json.load(f)
        
    with open('urls.json', 'r') as f:
        urls = json.load(f) 
        
    data = {
        "nodes": [],
        "edges": []
    }

    node = {}

    for di in visits:
        url = urls.get(str(di["url"]))
        visit_duration = di["visit_duration"]
    
        # 노드 url에 대한 총 방문 시간 계산
        if url not in node:
            node[url] = visit_duration 
        else:
            node[url] += visit_duration 
        
        # 이전 url
        from_url = urls.get(str(di.get("from_url")))
        if from_url is not None:
            if from_url != url :
                data["edges"].append({"source": from_url, "target": url})

    # 노드에 대한 정보 추가
    for key, value in node.items():
        if value <= 0:
            data["nodes"].append({"url": key, "spendtime": 1 })
        else  :
             data["nodes"].append({"url": key, "spendtime": value})
        
    # 그래프 데이터를 JSON 파일로 저장
    with open('graph.json', 'w') as f:
        json.dump(data, f, indent=4)
