import numpy as np

def hits_algorithm(k, eps):
    # 鄰接矩陣(Adjacency matrix) A
    A = np.array([[0, 1, 1, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
    # 初始化
    y = np.array([1, 1, 1, 1, 1])
    # 暫存上一次的結果
    x_temp = []
    y_temp = []
  
    for i in range(0, k):
        print(f'迭代第{i}次')
        # 計算 authority 值
        x = np.dot(A.T, y)
        # 計算 hub 值
        y = np.dot(A, x)
        """
        print(f'x: {x}')
        print(f'y: {y}')
        """
        # 正規化
        x = x / np.linalg.norm(x, ord=1)
        y = y / np.linalg.norm(y, ord=1)
        x_temp.append(x)
        y_temp.append(y)
        """
        print(f'x_temp: {x_temp}')
        print(f'y_temp{y_temp}')
        print(f'Normalized x:{x}')
        print(f'Normalized y:{y}')
        """
        if i >= 1:
          delta_authority = np.linalg.norm(x - x_temp[i-1], ord=1)
          delta_hub = np.linalg.norm(y - y_temp[i-1], ord=1)
          delta = np.sqrt(delta_hub ** 2 + delta_authority ** 2)
          print(f'delta: {delta}')
        # 如果delta小於等於epsilon，代表已收斂，結束迭代
          if delta <= eps:
            print('Converged!')
            x_temp.clear()
            y_temp.clear()
            break

    # 輸出正規化後的 authority 和 hub 值
    print("Normalized authority values: ", [round(i, 2) for i in x])
    print("Normalized hub values: ", [round(i, 2) for i in y])

def main():
    eps = 1.0e-6
    hits_algorithm(25, eps)

if __name__ == '__main__':
    main()