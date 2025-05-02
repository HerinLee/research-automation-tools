import pandas as pd

def clean_hr_data(file_path):
    """
    Clean heart rate data: remove NaNs, convert time, sort.
    """
    df = pd.read_csv(file_path)
    
    # 기본 처리
    df = df.dropna()
    if 'Time' in df.columns:
        df['Time'] = pd.to_datetime(df['Time'])
        df = df.sort_values('Time')

    return df

def summarize(df):
    """
    Print basic summary: head, column types, HR stats.
    """
    print("📊 Columns:", df.columns.tolist())
    if 'HR' in df.columns:
        print("💓 HR Mean:", df['HR'].mean())
        print("💓 HR Max:", df['HR'].max())
        print("💓 HR Min:", df['HR'].min())

if __name__ == "__main__":
    # 예시 경로 (샘플 파일 추가 시 수정)
    path = "raw_data_examples/sample_hr.csv"
    df = clean_hr_data(path)
    summarize(df)
