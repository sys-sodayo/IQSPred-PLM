import torch
from utils import evaluate_model_performance, roc

from model import CNN
from getdata import test_x,test_y

def  to_test_model (x,y):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CNN(64, 1280, 2).to(device)
    model.load_state_dict(torch.load("../model/model.pt"))
    model.eval()
    y = torch.tensor(y)

    pr_list,test_predictions = [],[]
    with torch.no_grad():
        for start in range(0, len(x), 40):
            inputs = x[start:start + 40].to(device)
            outputs = model(inputs)
            test_predictions.extend(torch.argmax(outputs, dim=-1).tolist())
            pr_list.extend(outputs[:, 1].cpu().numpy())  # Probability of positive class

    #performance evaluation metrics
    evaluate_model_performance(y, test_predictions)
    #ROC
    roc(y,pr_list)


if __name__ == "__main__":
    to_test_model(test_x,test_y)



