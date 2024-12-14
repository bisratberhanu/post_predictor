# Post Quality Prediction

## Demo Video
A you tube video is available at [here](https://youtu.be/-OUQesOfjVU)

This is a Django project called `prediction` that predicts the quality of a post for the platform [Mindplex.ai](https://mindplex.ai/). It accepts user reputation and interaction values and returns the predicted quality of the post.

## Project Structure

The Django project has a single app called `predict`. The project also includes a simple HTML file for user interaction, which can be found in the `templates` folder.

## Requirements

The project dependencies are listed in the `requirements.txt` file:

- django==4.2.7
- scikit-learn==1.3.2
- joblib==1.3.2
- numpy==1.26.2
- pandas==2.1.3

## Trained Model

The trained model is already included in the project and can be found at `post_quality_model.joblib`.

## Running the Project

To run the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```

2. Navigate to the `prediction` directory:
    ```sh
    cd prediction
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

5. Open your web browser and go to `http://127.0.0.1:8000/` to interact with the post quality predictor.

## Usage

The HTML form allows users to input their reputation and interaction values. Upon submission, the form sends a POST request to the server, which uses the trained model to predict the quality of the post and displays the result.

## License

This project is licensed under the MIT License.