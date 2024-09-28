## 코딩 문제 풀이
### 백준 문제
#### 1. 14719
구현에 가까운 문제
마지막 반례를 못 찾아서 틀렸었는데  제일 큰 값이 아니라 h 보다 크거나 같은 값에서 멈추고 인덱스를 업데이트하니까 풀렸다

#### 2. 2668
구현으로 풀려고 했는데 조건이 너무 복잡해져서 재귀로 해결했다

#### 3. 16236
시간 초과 + 입력 5,6 제대로 출력 안 됨

#### 4. 17144
미세먼지가 퍼지는 것은 bfs를 사용, 공기청정기를 돌리는 것은 반복문을 사용해 구현
반복문의 공통점을 찾아서 일반화할 수 있지만 시간 상 그냥 구현하는 걸로 해결함
+ 반복문 사용해서 일반화한 풀이 추가

#### 5. 17140
2차원 문제 -> 구현처럼 풀면 된다

#### 6. 77485
회전 시키는 문제 -> 구현

#### 7. 2805
이진탐색 -> s<=e가 중요 
마지막이 중요

#### 8. 15649
백트래킹
재귀 함수의 파라미터와 visited, 리스트 등을 잘 고려해서 공유해야 함

#### 9. 16987
broken된 것을 set으로 만들어서 계속 deepcopy 해서 파라미터로 넘기는 방법을 선택했는데
시간복잡도에서 걸릴 것 같다 → 계속 O(n)으로 카피하는 시간이 있으니까
새로운 리스트를 사용하지 않고 사용한다음 다시 원상태로 만들고 다음 계산을 하는 방식의 풀이다

#### 10. 14889
백트래킹으로 팀을 나눈 후에 점수차 min 구하기 -> 조합 같은 느낌