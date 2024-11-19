import torch
from utils import roc, evaluate_model_performance
from model import CNN
from getdata import  case_studies_x, case_studies_y

def  to_test_model (x,y):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CNN(64, 1280, 2).to(device)
    model.load_state_dict(torch.load("../model/MSRes-CNN.pt"))
    model.eval()
    y = torch.tensor(y)

    pr_list,test_predictions = [],[]
    with torch.no_grad():
        for start in range(0, len(x), 40):
            inputs = x[start:start + 40].to(device)
            outputs = model(inputs)
            test_predictions.extend(torch.argmax(outputs, dim=-1).tolist())
            pr_list.extend(outputs[:, 1].cpu().numpy())  # Probability of positive class
    return y, test_predictions


if __name__ == "__main__":
    y,test_predictions = to_test_model(case_studies_x, case_studies_y)
    for i in range(len(test_predictions)):
        print(y[i], test_predictions[i])



