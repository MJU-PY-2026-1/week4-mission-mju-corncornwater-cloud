# 파일이름 : main.py
# 작 성 자 :이재현
# 하 는 일 : 도장깨기! 맛집 버킷 리스트
# 1. 비어있는 리스트 만들기
bucket_list = [];
# 2. 입력 받고 리스트에 추가 하기 - 3번
bucket_list.append(input("맛집 리스트 입력:"));
bucket_list.append(input("맛집 리스트 입력:"));
bucket_list.append(input("맛집 리스트 입력:"));
#3. 리스트 출력
print(f'{"리스트: "}{bucket_list}');
#4. 맛집을 입력 받아 리스트 0 에 삽입
bucket_list.insert(0,input("맛집 리스트 추가:"));
#5. 리스트 출력
print(f'{"리스트: "}{bucket_list}');
#6. 도장깬 맛집을 입력 받아, 리스트에서 삭제
bucket_list.remove(input("도장 깨기:"));
#7. 리스트 출력 
print(f'{"리스트: "}{bucket_list}');
