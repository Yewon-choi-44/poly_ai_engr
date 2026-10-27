import torch

def split_train_test(x_tensor, y_tensor):
    torch.manual_seed(42)
    num_samples = x_tensor.shape[0]

    shuffle_indices = torch.randperm(num_samples)

    split_indices = int(num_samples * 0.7)

    train_indices = shuffle_indices[:split_indices]
    test_indices = shuffle_indices[split_indices:]

    x_train = x_tensor.iloc[train_indices]
    y_train = y_tensor.iloc[train_indices]
    x_test = x_tensor.iloc[test_indices]
    y_test = y_tensor.iloc[test_indices]

    return x_train, y_train, x_test, y_test