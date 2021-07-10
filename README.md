# machine_learning

## 강의
- 머신러닝, 딥러닝 기초 with Python, Keras.
https://www.edwith.org/pnu-deeplearning/joinLectures/27848

- 모두를 위한 머신러닝/딥러닝 강의.
https://hunkim.github.io/ml/

- MIT 6.S191 Introduction to Deep Learning.
http://introtodeeplearning.com/2020/index.html

## 실습

### 환경 구성 (Windows)
1. install anaconda (python과 numpy 등등 설치됨)
2. anaconda prompt 실행
3. install tensorflow 2.5.0rc0
```
pip install tensorflow==2.5.0rc0

ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory
위와 같은 에러 발생 시, 관리자 권한으로 실행하지 않았거나 directory가 너무 길어서 문제가 발생한 것이다.
Windows + R 키로 실행 창을 열고 regedit을 쳐서 레지스트리 관리창을 키고,
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem@LongPathsEnabled 를 1로 주어 경로의 길이 제한을 완화시킨다.
(참고: https://docs.python.org/3.7/using/windows.html#removing-the-max-path-limitation)

```
4. (GPU 사용을 위해서) CUDA 설치
5. (GPU 사용을 위해서) CuDNN 다운로드 후, dll 파일을 CUDA 설치된 directory의 bin 폴더에 넣음
