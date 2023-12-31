import fitz
from textblob import TextBlob
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import numpy as np

class FinancialAnalyzer:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.extract_text()

    def extract_text(self):
        doc = fitz.open(self.pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
        return text

    def analyze_sentiment(self):
        blob = TextBlob(self.text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score

    def generate_random_financial_data(self, num_data_points):
        # Example: Generate random financial data (replace with your actual data)
        categories = ['Revenue', 'Expenses', 'Profit', 'Cash Flow', 'Assets', 'Liabilities', 'Equity', 'Net Income']
        data = {category: np.random.randint(100000, 1000000, num_data_points) for category in categories}
        return data

    def plot_financial_metrics(self, data):
        # Example: Plotting financial metrics and saving as images
        categories = list(data.keys())
        num_data_points = len(data[categories[0]])
        for i in range(num_data_points):
            values = [data[category][i] for category in categories]
            plt.bar(categories, values)
            plt.title(f'Financial Metrics - Data Point {i + 1}')
            plt.xlabel('Categories')
            plt.ylabel('Values')
            image_path = f'financial_metrics_plot_{i + 1}.png'
            plt.savefig(image_path)
            plt.close()
            print(f"Saved plot as {image_path}")

    def display_credit_metrics(self, data):
        # Example: Creating a table for credit metrics
        credit_metrics_table = PrettyTable()
        credit_metrics_table.field_names = ['Metric', 'Mean Value']
        for category in data:
            mean_value = np.mean(data[category])
            credit_metrics_table.add_row([category, f'{mean_value:.2f}'])
        print(credit_metrics_table)

if __name__ == "__main__":
    pdf_path = "ENGIE_2022 Management report and annual consolidated financial statements.pdf"
    financial_analyzer = FinancialAnalyzer(pdf_path)

    # Example: Analyze sentiment
    sentiment_score = financial_analyzer.analyze_sentiment()
    print(f"Sentiment Score: {sentiment_score}")

    # Example: Generate random financial data
    num_data_points = 20
    financial_data = financial_analyzer.generate_random_financial_data(num_data_points)

    # Example: Plot financial metrics for each data point and save as images
    financial_analyzer.plot_financial_metrics(financial_data)

    # Example: Display credit metrics
    financial_analyzer.display_credit_metrics(financial_data)
