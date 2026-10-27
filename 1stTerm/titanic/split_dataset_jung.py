def splitFun(per, dataFrame):
    train_len = int(len(dataFrame) * per)
    x_train = dataFrame.iloc[:train_len, 1:]
    y_train = dataFrame.iloc[:train_len, 0]
    x_test = dataFrame.iloc[train_len:, 1:]
    y_test = dataFrame.iloc[train_len:, 0]
    return x_train, y_train, x_test, y_test