# Face_Mask_Detection

## Introduction:

In this project, I aimed to develop an end-to-end solution for face mask detection using a custom Convolutional Neural Network (CNN) model. The primary objective was to create a robust system capable of distinguishing between faces with masks and those without. To enhance user interaction and deployment, I employed Streamlit, a user-friendly Python library for building web applications with minimal effort.

## Custom CNN Model Architecture:

Unlike using pre-trained models, I designed a custom CNN architecture tailored to the specific requirements of face mask detection. The architecture comprised several convolutional layers to extract hierarchical features from the input images. Batch normalization and dropout layers were incorporated to improve the model's generalization capabilities and prevent overfitting.

## Training Process:

The dataset was split into training, validation, and testing sets to train and evaluate the model. During the training process, I utilized transfer learning techniques, initializing the model with random weights and fine-tuning it on the face mask dataset. The model was trained using an appropriate loss function, and optimization was performed using an adaptive learning rate.

## Streamlit Integration:

After successfully training the face mask detection model, I integrated it with Streamlit to create a user-friendly and interactive web application. Streamlit allowed me to design a simple yet powerful interface where users could upload images, and the model would instantly predict whether the faces in those images were masked or unmasked. The integration also included informative visualizations to enhance the user experience.

## Conclusion:

This project demonstrated the feasibility of building a custom CNN model for face mask detection without relying on pre-trained models. The integration of Streamlit facilitated the development of an end-to-end solution, making it user-friendly. The project contributes to the ongoing efforts in leveraging deep learning and web technologies for real-world applications, especially in the context of public health and safety.

# Video Presentation:-
[Project Recording,.webm](https://github.com/ParvSoni/Face_Mask_Detection/assets/123165567/15b394c9-d52e-4fea-9857-cb373d822006)
