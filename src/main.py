from datasets import load_dataset

if __name__ == "__main__":
    

    # 로컬 디렉토리에서 Parquet 파일 로드
    dataset = load_dataset(
        "parquet",
        data_files={
            "train": "data/lex_glue/ecthr_a/train-00000-of-00001.parquet",
            # "validation": "data/ecthr_a/validation/*.parquet",
            # "test": "data/ecthr_a/test/*.parquet"
        }
    )

    # 데이터 확인
    print(dataset["train"][0], '\n')

    # 전체 텍스트 길이 확인
    print(len(dataset['train'][0]['text']), '\n')

    # 맨 앞 세 문단
    print(dataset['train'][0]['text'][:3], '\n')

    # 맨 뒤 세 문단
    print(dataset['train'][0]['text'][-3:], '\n')
    
    # 훈련데이터는 총 몇 개?
    print(len(dataset["train"]), '\n')

    # 데이터셋의 features 확인
    print(dataset["train"].features, '\n')
    

    # print(dataset["validation"])
    # print(dataset["test"])
