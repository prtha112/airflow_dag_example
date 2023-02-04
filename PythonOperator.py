def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)   
    print(f"File pulled from {URL} and saved to {savepath}")

from airflow.operators.python_operator import PythonOperator

# Create the task
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={'URL':'http://xxxxxxx/xxxx.json', 'savepath':'xxxxxxxxx.json'},
    dag=process_sales_dag
)
