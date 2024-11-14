# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
# from tensorflow.keras.optimizers import Adam, SGD, RMSprop
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# import pandas as pd
# import numpy as np
# import cv2
# import os

# # Load CSV and map labels
# csv_path = 'output/dataset_labels.csv'
# df = pd.read_csv(csv_path)

# # Ensure 'Category' column can be used as labels and map to numerical values
# label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}
# df['label'] = df['Category'].map(label_mapping)

# # Load and preprocess images
# X = []
# y = []

# for index, row in df.iterrows():
#     image_path = row['Image Path']
#     label = row['label']
    
#     if os.path.exists(image_path):  # Check if the image file exists
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         if image is not None:  # Ensure the image was loaded successfully
#             image = cv2.resize(image, (128, 128)) / 255.0  # Resize and normalize
#             X.append(image)
#             y.append(label)
#         else:
#             print(f"Warning: Unable to load image at {image_path}")
#     else:
#         print(f"Warning: Image path {image_path} does not exist")

# # Convert to NumPy arrays
# X = np.array(X).reshape(-1, 128, 128, 1)  # Add channel dimension for grayscale
# y = np.array(y)

# # Convert labels to categorical (one-hot encoding)
# y = to_categorical(y, num_classes=len(label_mapping))

# # Split data into training, validation, and test sets
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# # Data augmentation
# datagen = ImageDataGenerator(
#     rotation_range=15,
#     width_shift_range=0.1,
#     height_shift_range=0.1,
#     horizontal_flip=True
# )
# datagen.fit(X_train)

# # Model architecture
# model = Sequential([
#     Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
#     MaxPooling2D(pool_size=(2, 2)),
#     Conv2D(64, (3, 3), activation='relu'),
#     MaxPooling2D(pool_size=(2, 2)),
#     Conv2D(128, (3, 3), activation='relu'),
#     MaxPooling2D(pool_size=(2, 2)),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dropout(0.5),
#     Dense(y_train.shape[1], activation='softmax')  # Adjust to number of classes
# ])

# # Compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# # Train the model with data augmentation
# history = model.fit(
#     datagen.flow(X_train, y_train, batch_size=32),
#     epochs=20,
#     validation_data=(X_val, y_val),
#     verbose=1
# )

# # Save the trained model
# model_path = 'models/trained_cnn_model.h5'
# os.makedirs(os.path.dirname(model_path), exist_ok=True)  # Ensure the directory exists
# model.save(model_path)
# print(f"Model trained and saved at {model_path}")

# # Model evaluation on the test set
# test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
# print(f"Test accuracy: {test_accuracy * 100:.2f}%")

# # Display label mapping for reference
# print("\nLabel mapping:")
# for label, idx in label_mapping.items():
#     print(f"{label}: {idx}")

# # Plot training history for better visualization
# import matplotlib.pyplot as plt

# plt.figure(figsize=(12, 4))

# # Plot accuracy
# plt.subplot(1, 2, 1)
# plt.plot(history.history['accuracy'], label='Training Accuracy')
# plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
# plt.title('Model Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()

# # Plot loss
# plt.subplot(1, 2, 2)
# plt.plot(history.history['loss'], label='Training Loss')
# plt.plot(history.history['val_loss'], label='Validation Loss')
# plt.title('Model Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()

# plt.show()
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn.metrics import classification_report
# from tensorflow.keras.optimizers import Adam, SGD, RMSprop
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# import pandas as pd
# import numpy as np
# import cv2
# import os
# import matplotlib.pyplot as plt

# # Load CSV and map labels
# csv_path = 'output/dataset_labels.csv'
# df = pd.read_csv(csv_path)

# # Ensure 'Category' column can be used as labels and map to numerical values
# label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}

# df['label'] = df['Category'].map(label_mapping)

# # Load and preprocess images
# X = []
# y = []

# for index, row in df.iterrows():
#     image_path = row['Image Path']
#     label = row['label']
    
#     if os.path.exists(image_path):  # Check if the image file exists
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         if image is not None:  # Ensure the image was loaded successfully
#             image = cv2.resize(image, (128, 128)) / 255.0  # Resize and normalize
#             X.append(image)
#             y.append(label)
#         else:
#             print(f"Warning: Unable to load image at {image_path}")
#     else:
#         print(f"Warning: Image path {image_path} does not exist")

# # Convert to NumPy arrays
# X = np.array(X).reshape(-1, 128, 128, 1)  # Add channel dimension for grayscale
# y = np.array(y)

# # Convert labels to categorical (one-hot encoding)
# y = to_categorical(y, num_classes=len(label_mapping))

# # Split data into training, validation, and test sets
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
# np.savez('output/test_data.npz', X_test=X_test, y_test=y_test)
# print("Test data saved to output/test_data.npz")

# # Data augmentation
# datagen = ImageDataGenerator(
#     rotation_range=30,         # Increased rotation
#     width_shift_range=0.2,     # Increased horizontal shift
#     height_shift_range=0.2,    # Increased vertical shift
#     shear_range=0.2,           # Added shear transformation
#     zoom_range=0.2,            # Added zoom transformation
#     horizontal_flip=True,      # Keep horizontal flip
#     vertical_flip=False        # Add if relevant for your dataset
# )
# datagen.fit(X_train)

# # Hyperparameter tuning
# batch_sizes = [16, 32, 64]
# learning_rates = [0.001, 0.0001]
# optimizers = [Adam, SGD, RMSprop]

# # Iterate through combinations of hyperparameters
# for batch_size in batch_sizes:
#     for lr in learning_rates:
#         for opt in optimizers:
#             print(f"Training with batch_size={batch_size}, learning_rate={lr}, optimizer={opt.__name__}")

#             model = Sequential([
#                 Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
#                 MaxPooling2D(pool_size=(2, 2)),
#                 Conv2D(64, (3, 3), activation='relu'),
#                 MaxPooling2D(pool_size=(2, 2)),
#                 Conv2D(128, (3, 3), activation='relu'),
#                 MaxPooling2D(pool_size=(2, 2)),
#                 Flatten(),
#                 Dense(128, activation='relu'),
#                 Dropout(0.5),
#                 Dense(y_train.shape[1], activation='softmax')  # Adjust to number of classes
#             ])

#             optimizer = opt(learning_rate=lr)
#             model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

#             # Train the model with data augmentation
#             history = model.fit(
#                 datagen.flow(X_train, y_train, batch_size=batch_size),
#                 epochs=10,  # Use a smaller number of epochs for testing hyperparameters quickly
#                 validation_data=(X_val, y_val),
#                 verbose=1
#             )

#             # Save each trained model with unique hyperparameters
#             model_path = f'models/trained_cnn_{opt.__name__}_lr{lr}_bs{batch_size}.h5'
#             os.makedirs(os.path.dirname(model_path), exist_ok=True)  # Ensure the directory exists
#             model.save(model_path)
#             print(f"Model trained and saved at {model_path}")

#             # Evaluate the model on the test set
#             test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
#             print(f"Test accuracy with batch_size={batch_size}, learning_rate={lr}, optimizer={opt.__name__}: {test_accuracy * 100:.2f}%")

#             # Predict on the test set
#             y_pred = model.predict(X_test)
#             y_pred_classes = np.argmax(y_pred, axis=1)
#             y_true_classes = np.argmax(y_test, axis=1)

#             # Print classification report
#             print(classification_report(y_true_classes, y_pred_classes, target_names=label_mapping.keys()))

#             # Plot training history for better visualization
#             plt.figure(figsize=(12, 4))
            
#             # Plot accuracy
#             plt.subplot(1, 2, 1)
#             plt.plot(history.history['accuracy'], label='Training Accuracy')
#             plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
#             plt.title(f'Model Accuracy (lr={lr}, bs={batch_size}, opt={opt.__name__})')
#             plt.xlabel('Epochs')
#             plt.ylabel('Accuracy')
#             plt.legend()

#             # Plot loss
#             plt.subplot(1, 2, 2)
#             plt.plot(history.history['loss'], label='Training Loss')
#             plt.plot(history.history['val_loss'], label='Validation Loss')
#             plt.title(f'Model Loss (lr={lr}, bs={batch_size}, opt={opt.__name__})')
#             plt.xlabel('Epochs')
#             plt.ylabel('Loss')
#             plt.legend()

#             plt.show()

# # Display label mapping for reference
# print("\nLabel mapping:")
# for label, idx in label_mapping.items():
#     print(f"{label}: {idx}")

# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn.metrics import classification_report
# from tensorflow.keras.optimizers import Adam
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# import pandas as pd
# import numpy as np
# import cv2
# import os
# import matplotlib.pyplot as plt
# import json
# from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
# from sklearn.utils.class_weight import compute_class_weight

# # Load CSV and map labels
# csv_path = 'output/dataset_labels.csv'
# df = pd.read_csv(csv_path)

# # Map labels for 'Category' (sequence type) and 'Disease Label'
# label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}
# disease_label_mapping = {label: idx for idx, label in enumerate(df['Disease Label'].unique())}

# df['label'] = df['Category'].map(label_mapping)
# df['disease_label'] = df['Disease Label'].map(disease_label_mapping)

# # Load and preprocess images
# X = []
# y_sequence = []
# y_disease = []

# for index, row in df.iterrows():
#     image_path = row['Image Path']
#     sequence_label = row['label']
#     disease_label = row['disease_label']
    
#     if os.path.exists(image_path):
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         if image is not None:
#             image = cv2.resize(image, (128, 128)) / 255.0
#             X.append(image)
#             y_sequence.append(sequence_label)
#             y_disease.append(disease_label)
#         else:
#             print(f"Warning: Unable to load image at {image_path}")
#     else:
#         print(f"Warning: Image path {image_path} does not exist")

# # Convert to NumPy arrays
# X = np.array(X).reshape(-1, 128, 128, 1)
# y_sequence = np.array(y_sequence)
# y_disease = np.array(y_disease)

# # Ensure the lengths match
# assert len(X) == len(y_sequence) == len(y_disease), "Mismatch in the number of samples between X, y_sequence, and y_disease."

# # Convert labels to categorical (one-hot encoding)
# y_sequence = to_categorical(y_sequence, num_classes=len(label_mapping))
# y_disease = to_categorical(y_disease, num_classes=len(disease_label_mapping))

# # Split data into training, validation, and test sets
# X_train, X_temp, y_sequence_train, y_sequence_temp, y_disease_train, y_disease_temp = train_test_split(
#     X, y_sequence, y_disease, test_size=0.3, random_state=42
# )
# X_val, X_test, y_sequence_val, y_sequence_test, y_disease_val, y_disease_test = train_test_split(
#     X_temp, y_sequence_temp, y_disease_temp, test_size=0.5, random_state=42
# )

# # Save test data for later evaluation
# np.savez('output/test_data.npz', X_test=X_test, y_sequence_test=y_sequence_test, y_disease_test=y_disease_test)
# print("Test data saved to output/test_data.npz")

# # Data augmentation
# datagen = ImageDataGenerator(
#     rotation_range=30,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     vertical_flip=False
# )
# datagen.fit(X_train)

# # Calculate class weights to handle imbalanced data
# y_seq_flat = np.argmax(y_sequence_train, axis=1)
# y_dis_flat = np.argmax(y_disease_train, axis=1)

# class_weights_seq = compute_class_weight('balanced', classes=np.unique(y_seq_flat), y=y_seq_flat)
# class_weights_disease = compute_class_weight('balanced', classes=np.unique(y_dis_flat), y=y_dis_flat)

# # Create dictionaries for class weights
# class_weights_seq_dict = dict(enumerate(class_weights_seq))
# class_weights_disease_dict = dict(enumerate(class_weights_disease))

# # Custom generator for multi-output data with sample weights
# def multi_output_generator(generator, X, y1, y2, class_weights_seq, class_weights_disease, batch_size):
#     gen = generator.flow(X, y1, batch_size=batch_size, seed=42)
#     while True:
#         X_batch, y1_batch = next(gen)
#         indices = gen.index_array[:len(X_batch)]
#         y2_batch = y2[indices]

#         # Calculate sample weights for both outputs
#         sample_weights_seq = np.array([class_weights_seq[np.argmax(label)] for label in y1_batch])
#         sample_weights_disease = np.array([class_weights_disease[np.argmax(label)] for label in y2_batch])

#         # Combine sample weights (average)
#         combined_sample_weights = np.mean([sample_weights_seq, sample_weights_disease], axis=0)

#         yield X_batch, {'sequence_output': y1_batch, 'disease_output': y2_batch}, combined_sample_weights

# # Define a multi-output CNN model
# input_layer = Input(shape=(128, 128, 1))
# x = Conv2D(32, (3, 3), activation='relu')(input_layer)
# x = MaxPooling2D(pool_size=(2, 2))(x)
# x = Conv2D(64, (3, 3), activation='relu')(x)
# x = MaxPooling2D(pool_size=(2, 2))(x)
# x = Conv2D(128, (3, 3), activation='relu')(x)
# x = MaxPooling2D(pool_size=(2, 2))(x)
# x = Flatten()(x)
# x = Dense(128, activation='relu')(x)
# x = Dropout(0.5)(x)

# # Output layers for sequence type and disease label
# sequence_output = Dense(len(label_mapping), activation='softmax', name='sequence_output')(x)
# disease_output = Dense(len(disease_label_mapping), activation='softmax', name='disease_output')(x)

# # Define the model
# model = Model(inputs=input_layer, outputs=[sequence_output, disease_output])

# # Compile the model with metrics and optimizer
# model.compile(optimizer=Adam(learning_rate=0.001),
#               loss={'sequence_output': 'categorical_crossentropy', 'disease_output': 'categorical_crossentropy'},
#               metrics={'sequence_output': 'accuracy', 'disease_output': 'accuracy'})

# # Callbacks for saving the best model and early stopping
# checkpoint = ModelCheckpoint('models/best_model.keras', monitor='val_loss', save_best_only=True)
# early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# # Train the model using the custom generator
# history = model.fit(
#     multi_output_generator(datagen, X_train, y_sequence_train, y_disease_train, class_weights_seq_dict, class_weights_disease_dict, batch_size=32),
#     steps_per_epoch=len(X_train) // 32,
#     epochs=20,
#     validation_data=(X_val, {'sequence_output': y_sequence_val, 'disease_output': y_disease_val}),
#     callbacks=[checkpoint, early_stopping],
#     verbose=1
# )

# # Save the trained model
# model_path = 'models/trained_multioutput_model.keras'
# os.makedirs(os.path.dirname(model_path), exist_ok=True)
# model.save(model_path)
# print(f"Model trained and saved at {model_path}")

# # Evaluate the model on the test set
# test_loss = model.evaluate(X_test, {'sequence_output': y_sequence_test, 'disease_output': y_disease_test}, verbose=0)
# print(f"Test loss: {test_loss}")
# print(f"Sequence Loss: {test_loss[1]:.4f}")
# print(f"Disease Loss: {test_loss[2]:.4f}")

# # Print classification reports
# y_pred = model.predict(X_test)
# y_pred_sequence = np.argmax(y_pred[0], axis=1)
# y_pred_disease = np.argmax(y_pred[1], axis=1)
# y_true_sequence = np.argmax(y_sequence_test, axis=1)
# y_true_disease = np.argmax(y_disease_test, axis=1)

# print("\nSequence Classification Report:")
# sequence_report = classification_report(y_true_sequence, y_pred_sequence, target_names=label_mapping.keys(), output_dict=True)
# sequence_report_df = pd.DataFrame(sequence_report).transpose()
# print(sequence_report_df)

# print("\nDisease Classification Report:")
# disease_report = classification_report(y_true_disease, y_pred_disease, target_names=disease_label_mapping.keys(), output_dict=True)
# disease_report_df = pd.DataFrame(disease_report).transpose()
# print(disease_report_df)

# # Plot training history
# sequence_acc = history.history['sequence_output_accuracy']
# val_sequence_acc = history.history['val_sequence_output_accuracy']
# sequence_loss = history.history['sequence_output_loss']
# val_sequence_loss = history.history['val_sequence_output_loss']

# disease_acc = history.history['disease_output_accuracy']
# val_disease_acc = history.history['val_disease_output_accuracy']
# disease_loss = history.history['disease_output_loss']
# val_disease_loss = history.history['val_disease_output_loss']

# plt.figure(figsize=(14, 6))

# plt.subplot(2, 2, 1)
# plt.plot(sequence_acc, label='Training Sequence Accuracy')
# plt.plot(val_sequence_acc, label='Validation Sequence Accuracy')
# plt.title('Sequence Output Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()

# plt.subplot(2, 2, 2)
# plt.plot(sequence_loss, label='Training Sequence Loss')
# plt.plot(val_sequence_loss, label='Validation Sequence Loss')
# plt.title('Sequence Output Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()

# plt.subplot(2, 2, 3)
# plt.plot(disease_acc, label='Training Disease Accuracy')
# plt.plot(val_disease_acc, label='Validation Disease Accuracy')
# plt.title('Disease Output Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()

# plt.subplot(2, 2, 4)
# plt.plot(disease_loss, label='Training Disease Loss')
# plt.plot(val_disease_loss, label='Validation Disease Loss')
# plt.title('Disease Output Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()

# plt.tight_layout()
# plt.show()

# # Display label mapping and diseases for reference
# print("\nLabel mapping and associated diseases:")
# for label, idx in label_mapping.items():
#     print(f"{label} ({idx}): {disease_label_mapping.get(label, 'N/A')}")

# # Save label_mapping and disease_label_mapping
# with open('models/label_mapping.json', 'w') as f:
#     json.dump(label_mapping, f)

# with open('models/disease_label_mapping.json', 'w') as f:
#     json.dump(disease_label_mapping, f)

# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn.metrics import classification_report, confusion_matrix
# from tensorflow.keras.optimizers import Adam, SGD, RMSprop
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# import pandas as pd
# import numpy as np
# import cv2
# import os
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load CSV and map labels
# csv_path = 'output/dataset_labels.csv'
# df = pd.read_csv(csv_path)

# # Ensure 'Category' column can be used as labels and map to numerical values
# label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}
# df['label'] = df['Category'].map(label_mapping)

# # Create a mapping of label indices to disease labels
# disease_mapping = {}
# for index, row in df.iterrows():
#     category = row['Category']
#     disease = row['Disease Label']  # Ensure this column exists in your CSV
#     if label_mapping[category] not in disease_mapping:
#         disease_mapping[label_mapping[category]] = set()
#     disease_mapping[label_mapping[category]].add(disease)

# # Load and preprocess images
# X = []
# y = []

# for index, row in df.iterrows():
#     image_path = row['Image Path']
#     label = row['label']
    
#     if os.path.exists(image_path):  # Check if the image file exists
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         if image is not None:  # Ensure the image was loaded successfully
#             image = cv2.resize(image, (128, 128)) / 255.0  # Resize and normalize
#             X.append(image)
#             y.append(label)
#         else:
#             print(f"Warning: Unable to load image at {image_path}")
#     else:
#         print(f"Warning: Image path {image_path} does not exist")

# # Convert to NumPy arrays
# X = np.array(X).reshape(-1, 128, 128, 1)  # Add channel dimension for grayscale
# y = np.array(y)

# # Convert labels to categorical (one-hot encoding)
# y = to_categorical(y, num_classes=len(label_mapping))

# # Split data into training, validation, and test sets
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
# np.savez('output/test_data.npz', X_test=X_test, y_test=y_test)
# print("Test data saved to output/test_data.npz")

# # Data augmentation
# datagen = ImageDataGenerator(
#     rotation_range=30,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True
# )
# datagen.fit(X_train)

# # Hyperparameter tuning (reduced for simplicity)
# batch_sizes = [32]
# learning_rates = [0.001]
# optimizers = [Adam]

# # Training and evaluation loop
# for batch_size in batch_sizes:
#     for lr in learning_rates:
#         for opt in optimizers:
#             print(f"Training with batch_size={batch_size}, learning_rate={lr}, optimizer={opt.__name__}")

#             model = Sequential([
#                 Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
#                 MaxPooling2D(pool_size=(2, 2)),
#                 Conv2D(64, (3, 3), activation='relu'),
#                 MaxPooling2D(pool_size=(2, 2)),
#                 Conv2D(128, (3, 3), activation='relu'),
#                 MaxPooling2D(pool_size=(2, 2)),
#                 Flatten(),
#                 Dense(128, activation='relu'),
#                 Dropout(0.5),
#                 Dense(y_train.shape[1], activation='softmax')
#             ])

#             optimizer = opt(learning_rate=lr)
#             model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

#             history = model.fit(
#                 datagen.flow(X_train, y_train, batch_size=batch_size),
#                 epochs=5,  # For brevity; adjust as needed
#                 validation_data=(X_val, y_val),
#                 verbose=1
#             )

#             # Save the model
#             model_path = f'models/trained_cnn_{opt.__name__}_lr{lr}_bs{batch_size}.h5'
#             os.makedirs(os.path.dirname(model_path), exist_ok=True)
#             model.save(model_path)
#             print(f"Model trained and saved at {model_path}")

#             # Evaluate the model
#             test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
#             print(f"Test accuracy with batch_size={batch_size}, learning_rate={lr}, optimizer={opt.__name__}: {test_accuracy * 100:.2f}%")

#             # Predict and map to disease labels
#             y_pred = model.predict(X_test)
#             y_pred_classes = np.argmax(y_pred, axis=1)
#             y_true_classes = np.argmax(y_test, axis=1)

#             # Print classification report
#             report = classification_report(y_true_classes, y_pred_classes, target_names=label_mapping.keys())
#             print("\nClassification Report:")
#             print(report)

#             # Plot confusion matrix
#             cm = confusion_matrix(y_true_classes, y_pred_classes)
#             plt.figure(figsize=(10, 8))
#             sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_mapping.keys(), yticklabels=label_mapping.keys())
#             plt.title(f'Confusion Matrix (lr={lr}, bs={batch_size}, opt={opt.__name__})')
#             plt.xlabel('Predicted')
#             plt.ylabel('True')
#             plt.show()

#             # Plot training history
#             plt.figure(figsize=(12, 4))

#             # Plot accuracy
#             plt.subplot(1, 2, 1)
#             plt.plot(history.history['accuracy'], label='Training Accuracy')
#             plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
#             plt.title(f'Model Accuracy (lr={lr}, bs={batch_size}, opt={opt.__name__})')
#             plt.xlabel('Epochs')
#             plt.ylabel('Accuracy')
#             plt.legend()

#             # Plot loss
#             plt.subplot(1, 2, 2)
#             plt.plot(history.history['loss'], label='Training Loss')
#             plt.plot(history.history['val_loss'], label='Validation Loss')
#             plt.title(f'Model Loss (lr={lr}, bs={batch_size}, opt={opt.__name__})')
#             plt.xlabel('Epochs')
#             plt.ylabel('Loss')
#             plt.legend()

#             plt.show()

#             # Print the predicted labels and associated diseases
#             print("\nPredicted categories and their associated diseases:")
#             for pred, true in zip(y_pred_classes, y_true_classes):
#                 category_name = list(label_mapping.keys())[list(label_mapping.values()).index(true)]
#                 predicted_diseases = disease_mapping[pred]
#                 print(f"Image classified as '{category_name}' with diseases: {predicted_diseases}")

# # Display label mapping and diseases for reference
# print("\nLabel mapping and associated diseases:")
# for label, idx in label_mapping.items():
#     print(f"{label} ({idx}): {disease_mapping[idx]}")

# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn.metrics import classification_report
# from tensorflow.keras.optimizers import Adam
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# import pandas as pd
# import numpy as np
# import cv2
# import os
# import matplotlib.pyplot as plt
# import json
# from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
# from sklearn.utils.class_weight import compute_class_weight

# # Load CSV and map labels
# csv_path = 'output/dataset_labels.csv'
# df = pd.read_csv(csv_path)

# # Filter out UNKNOWN entries
# df = df[(df['Category'] != 'UNKNOWN') & 
#         (df['Disease Label'] != 'UNKNOWN') & 
#         (df['Sequence Name'] != 'UNKNOWN')]

# # Recreate the label mappings to exclude 'UNKNOWN'
# label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}
# disease_label_mapping = {label: idx for idx, label in enumerate(df['Disease Label'].unique())}
# sequence_tag_mapping = {tag: idx for idx, tag in enumerate(df['Sequence Name'].unique())}

# # Map labels after filtering
# df['label'] = df['Category'].map(label_mapping)
# df['disease_label'] = df['Disease Label'].map(disease_label_mapping)
# df['sequence_tag_label'] = df['Sequence Name'].map(sequence_tag_mapping)


# # Load and preprocess images
# X, y_sequence, y_disease, sequence_tags = [], [], [], []

# for index, row in df.iterrows():
#     image_path = row['Image Path']
#     sequence_label = row['label']
#     disease_label = row['disease_label']
#     sequence_tag_label = row['sequence_tag_label']

#     if os.path.exists(image_path):
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         if image is not None:
#             image = cv2.resize(image, (128, 128)) / 255.0
#             X.append(image)
#             y_sequence.append(sequence_label)
#             y_disease.append(disease_label)
#             sequence_tags.append(sequence_tag_label)
#         else:
#             print(f"Warning: Unable to load image at {image_path}")
#     else:
#         print(f"Warning: Image path {image_path} does not exist")

# # Convert to NumPy arrays
# X = np.array(X).reshape(-1, 128, 128, 1)
# y_sequence = np.array(y_sequence)
# y_disease = np.array(y_disease)
# sequence_tags = np.array(sequence_tags)

# # Convert labels to categorical (one-hot encoding)
# y_sequence = to_categorical(y_sequence, num_classes=len(label_mapping))
# y_disease = to_categorical(y_disease, num_classes=len(disease_label_mapping))
# sequence_tags_onehot = to_categorical(sequence_tags, num_classes=len(sequence_tag_mapping))

# # Split data into training, validation, and test sets
# X_train, X_temp, y_sequence_train, y_sequence_temp, y_disease_train, y_disease_temp, seq_tags_train, seq_tags_temp = train_test_split(
#     X, y_sequence, y_disease, sequence_tags_onehot, test_size=0.3, random_state=42
# )
# X_val, X_test, y_sequence_val, y_sequence_test, y_disease_val, y_disease_test, seq_tags_val, seq_tags_test = train_test_split(
#     X_temp, y_sequence_temp, y_disease_temp, seq_tags_temp, test_size=0.5, random_state=42
# )

# # Save test data for later evaluation
# np.savez('output/test_data.npz', X_test=X_test, y_sequence_test=y_sequence_test, y_disease_test=y_disease_test, seq_tags_test=seq_tags_test)
# print("Test data saved to output/test_data.npz")

# # Data augmentation
# datagen = ImageDataGenerator(
#     rotation_range=30,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True
# )
# datagen.fit(X_train)

# # Calculate class weights for imbalanced data
# y_seq_flat = np.argmax(y_sequence_train, axis=1)
# y_dis_flat = np.argmax(y_disease_train, axis=1)

# class_weights_seq = compute_class_weight('balanced', classes=np.unique(y_seq_flat), y=y_seq_flat)
# class_weights_disease = compute_class_weight('balanced', classes=np.unique(y_dis_flat), y=y_dis_flat)

# # Create dictionaries for class weights
# class_weights_seq_dict = dict(enumerate(class_weights_seq))
# class_weights_disease_dict = dict(enumerate(class_weights_disease))

# # Custom generator for multi-output data with sample weights
# def multi_output_generator(generator, X, y1, y2, seq_tags, class_weights_seq, class_weights_disease, batch_size):
#     gen = generator.flow(X, y1, batch_size=batch_size, seed=42)
#     while True:
#         X_batch, y1_batch = next(gen)
#         indices = gen.index_array[:len(X_batch)]
#         y2_batch = y2[indices]
#         seq_tags_batch = seq_tags[indices]

#         # Calculate sample weights for both outputs
#         sample_weights_seq = np.array([class_weights_seq[np.argmax(label)] for label in y1_batch])
#         sample_weights_disease = np.array([class_weights_disease[np.argmax(label)] for label in y2_batch])

#         # Combine sample weights (average)
#         combined_sample_weights = np.mean([sample_weights_seq, sample_weights_disease], axis=0)

#         yield X_batch, {'sequence_output': y1_batch, 'disease_output': y2_batch, 'seq_tag_output': seq_tags_batch}, combined_sample_weights

# # Define a multi-output CNN model
# input_layer = Input(shape=(128, 128, 1))
# x = Conv2D(32, (3, 3), activation='relu')(input_layer)
# x = MaxPooling2D(pool_size=(2, 2))(x)
# x = Conv2D(64, (3, 3), activation='relu')(x)
# x = MaxPooling2D(pool_size=(2, 2))(x)
# x = Conv2D(128, (3, 3), activation='relu')(x)
# x = MaxPooling2D(pool_size=(2, 2))(x)
# x = Flatten()(x)
# x = Dense(128, activation='relu')(x)
# x = Dropout(0.5)(x)

# # Output layers
# sequence_output = Dense(len(label_mapping), activation='softmax', name='sequence_output')(x)
# seq_tag_output = Dense(len(sequence_tag_mapping), activation='softmax', name='seq_tag_output')(x)
# disease_output = Dense(len(disease_label_mapping), activation='softmax', name='disease_output')(x)

# # Define the model
# model = Model(inputs=input_layer, outputs=[sequence_output, seq_tag_output, disease_output])

# # Compile the model
# model.compile(optimizer=Adam(learning_rate=0.001),
#               loss={'sequence_output': 'categorical_crossentropy',
#                     'seq_tag_output': 'categorical_crossentropy',
#                     'disease_output': 'categorical_crossentropy'},
#               metrics={'sequence_output': 'accuracy',
#                        'seq_tag_output': 'accuracy',
#                        'disease_output': 'accuracy'})

# # Callbacks
# checkpoint = ModelCheckpoint('models/best_model.keras', monitor='val_loss', save_best_only=True)
# early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# # Train the model
# history = model.fit(
#     multi_output_generator(datagen, X_train, y_sequence_train, y_disease_train, seq_tags_train, class_weights_seq_dict, class_weights_disease_dict, batch_size=32),
#     steps_per_epoch=len(X_train) // 32,
#     epochs=20,
#     validation_data=(X_val, {'sequence_output': y_sequence_val, 'seq_tag_output': seq_tags_val, 'disease_output': y_disease_val}),
#     callbacks=[checkpoint, early_stopping],
#     verbose=1
# )

# # Save the model
# model_path = 'models/trained_multioutput_model.keras'
# os.makedirs(os.path.dirname(model_path), exist_ok=True)
# model.save(model_path)
# print(f"Model trained and saved at {model_path}")

# # Evaluate on the test set
# test_loss = model.evaluate(X_test, {'sequence_output': y_sequence_test, 'seq_tag_output': seq_tags_test, 'disease_output': y_disease_test}, verbose=0)
# print(f"Test loss: {test_loss}")
# print(f"Sequence Loss: {test_loss[1]:.4f}")
# print(f"Seq Tag Loss: {test_loss[2]:.4f}")
# print(f"Disease Loss: {test_loss[3]:.4f}")

# # Print classification reports
# y_pred = model.predict(X_test)
# y_pred_sequence = np.argmax(y_pred[0], axis=1)
# y_pred_seq_tag = np.argmax(y_pred[1], axis=1)
# y_pred_disease = np.argmax(y_pred[2], axis=1)

# y_true_sequence = np.argmax(y_sequence_test, axis=1)
# y_pred_seq_tag = np.argmax(seq_tags_test, axis=1)
# y_true_disease = np.argmax(y_disease_test, axis=1)

# # Extract unique labels from y_pred_seq_tag for validation
# unique_labels_seq_tag = np.unique(y_pred_seq_tag)

# # Create filtered target names based on unique labels in y_pred_seq_tag
# filtered_target_names_seq_tag = [
#     sequence_tag_mapping[idx] for idx in unique_labels_seq_tag if idx in sequence_tag_mapping
# ]

# # Ensure that the length of filtered_target_names_seq_tag matches the unique labels in y_pred_seq_tag
# if len(filtered_target_names_seq_tag) != len(unique_labels_seq_tag):
#     print("Warning: Some unique labels in y_pred_seq_tag do not have corresponding names in sequence_tag_mapping.")
#     filtered_target_names_seq_tag = [str(idx) for idx in unique_labels_seq_tag]  # Fallback to using indices

# # Print classification report for sequence tags with corrected labels and target names
# print("\nSequence Name Classification Report:")
# try:
#     seq_tag_report = classification_report(
#         y_pred_seq_tag,
#         y_pred_seq_tag,
#         labels=unique_labels_seq_tag,  # Ensure labels match unique y_pred_seq_tag entries
#         target_names=filtered_target_names_seq_tag,  # Ensure target names match the unique labels
#         output_dict=True
#     )
#     seq_tag_report_df = pd.DataFrame(seq_tag_report).transpose()
#     print(seq_tag_report_df)
# except ValueError as e:
#     print(f"Error generating sequence tag classification report: {e}")

# # Print other classification reports
# print("\nSequence Classification Report:")
# sequence_report = classification_report(y_true_sequence, y_pred_sequence, target_names=list(label_mapping.keys()), output_dict=True)
# sequence_report_df = pd.DataFrame(sequence_report).transpose()
# print(sequence_report_df)

# print("\nDisease Classification Report:")
# disease_report = classification_report(y_true_disease, y_pred_disease, target_names=list(disease_label_mapping.keys()), output_dict=True)
# disease_report_df = pd.DataFrame(disease_report).transpose()
# print(disease_report_df)


# # Plot training history
# plt.figure(figsize=(14, 8))

# plt.subplot(3, 2, 1)
# plt.plot(history.history['sequence_output_accuracy'], label='Training Sequence Accuracy')
# plt.plot(history.history['val_sequence_output_accuracy'], label='Validation Sequence Accuracy')
# plt.title('Sequence Output Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()

# plt.subplot(3, 2, 2)
# plt.plot(history.history['sequence_output_loss'], label='Training Sequence Loss')
# plt.plot(history.history['val_sequence_output_loss'], label='Validation Sequence Loss')
# plt.title('Sequence Output Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()

# plt.subplot(3, 2, 3)
# plt.plot(history.history['seq_tag_output_accuracy'], label='Training Seq Tag Accuracy')
# plt.plot(history.history['val_seq_tag_output_accuracy'], label='Validation Seq Tag Accuracy')
# plt.title('Seq Tag Output Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()

# plt.subplot(3, 2, 4)
# plt.plot(history.history['seq_tag_output_loss'], label='Training Seq Tag Loss')
# plt.plot(history.history['val_seq_tag_output_loss'], label='Validation Seq Tag Loss')
# plt.title('Seq Tag Output Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()

# plt.subplot(3, 2, 5)
# plt.plot(history.history['disease_output_accuracy'], label='Training Disease Accuracy')
# plt.plot(history.history['val_disease_output_accuracy'], label='Validation Disease Accuracy')
# plt.title('Disease Output Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()

# plt.subplot(3, 2, 6)
# plt.plot(history.history['disease_output_loss'], label='Training Disease Loss')
# plt.plot(history.history['val_disease_output_loss'], label='Validation Disease Loss')
# plt.title('Disease Output Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()

# plt.tight_layout()
# plt.show()

# # Save mappings
# with open('models/label_mapping.json', 'w') as f:
#     json.dump(label_mapping, f)

# with open('models/disease_label_mapping.json', 'w') as f:
#     json.dump(disease_label_mapping, f)

# with open('models/sequence_tag_mapping.json', 'w') as f:
#     json.dump(sequence_tag_mapping, f)


from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras._tf_keras.keras.utils import to_categorical
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import cv2
import os
import json
from keras._tf_keras.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.utils.class_weight import compute_class_weight
import matplotlib.pyplot as plt
from preprocessing_utils import preprocess_image 


# Load CSV and map labels
csv_path = 'output/dataset_labels.csv'
df = pd.read_csv(csv_path)

# Filter out UNKNOWN entries
df = df[(df['Category'] != 'UNKNOWN') & 
        (df['Disease Label'] != 'UNKNOWN') & 
        (df['Sequence Name'] != 'UNKNOWN')]

# Create label mappings excluding 'UNKNOWN'
label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}
disease_label_mapping = {label: idx for idx, label in enumerate(df['Disease Label'].unique())}
sequence_tag_mapping = {tag: idx for idx, tag in enumerate(df['Sequence Name'].unique())}

# Reverse mappings for label interpretation
label_mapping_rev = {v: k for k, v in label_mapping.items()}
disease_label_mapping_rev = {v: k for k, v in disease_label_mapping.items()}
sequence_tag_mapping_rev = {v: k for k, v in sequence_tag_mapping.items()}

# Map labels in the DataFrame
df['label'] = df['Category'].map(label_mapping)
df['disease_label'] = df['Disease Label'].map(disease_label_mapping)
df['sequence_tag_label'] = df['Sequence Name'].map(sequence_tag_mapping)

# Load and preprocess images
X, y_sequence, y_disease, sequence_tags = [], [], [], []

for index, row in df.iterrows():
    image_path = row['Image Path']
    sequence_label = row['label']
    disease_label = row['disease_label']
    sequence_tag_label = row['sequence_tag_label']

    if os.path.exists(image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            image = preprocess_image(image_path, is_dicom=False) 
            X.append(image[0])
            y_sequence.append(sequence_label)
            y_disease.append(disease_label)
            sequence_tags.append(sequence_tag_label)
        else:
            print(f"Warning: Unable to load image at {image_path}")
    else:
        print(f"Warning: Image path {image_path} does not exist")

# Convert to NumPy arrays
X = np.array(X).reshape(-1, 128, 128, 1)
y_sequence = np.array(y_sequence)
y_disease = np.array(y_disease)
sequence_tags = np.array(sequence_tags)

# Convert labels to categorical (one-hot encoding)
y_sequence = to_categorical(y_sequence, num_classes=len(label_mapping))
y_disease = to_categorical(y_disease, num_classes=len(disease_label_mapping))
sequence_tags_onehot = to_categorical(sequence_tags, num_classes=len(sequence_tag_mapping))

# Split data into training, validation, and test sets
X_train, X_temp, y_sequence_train, y_sequence_temp, y_disease_train, y_disease_temp, seq_tags_train, seq_tags_temp = train_test_split(
    X, y_sequence, y_disease, sequence_tags_onehot, test_size=0.3, random_state=42
)
X_val, X_test, y_sequence_val, y_sequence_test, y_disease_val, y_disease_test, seq_tags_val, seq_tags_test = train_test_split(
    X_temp, y_sequence_temp, y_disease_temp, seq_tags_temp, test_size=0.5, random_state=42
)

# Save test data for later evaluation
np.savez('output/test_data.npz', X_test=X_test, y_sequence_test=y_sequence_test, y_disease_test=y_disease_test, seq_tags_test=seq_tags_test)
print("Test data saved to output/test_data.npz")

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
datagen.fit(X_train)

# Calculate class weights for imbalanced data
y_seq_flat = np.argmax(y_sequence_train, axis=1)
y_dis_flat = np.argmax(y_disease_train, axis=1)

class_weights_seq = compute_class_weight('balanced', classes=np.unique(y_seq_flat), y=y_seq_flat)
class_weights_disease = compute_class_weight('balanced', classes=np.unique(y_dis_flat), y=y_dis_flat)

# Create dictionaries for class weights
class_weights_seq_dict = dict(enumerate(class_weights_seq))
class_weights_disease_dict = dict(enumerate(class_weights_disease))

# Custom generator for multi-output data with sample weights
def multi_output_generator(generator, X, y1, y2, seq_tags, class_weights_seq, class_weights_disease, batch_size):
    gen = generator.flow(X, y1, batch_size=batch_size, seed=42)
    while True:
        X_batch, y1_batch = next(gen)
        indices = gen.index_array[:len(X_batch)]
        y2_batch = y2[indices]
        seq_tags_batch = seq_tags[indices]

        # Calculate sample weights for both outputs
        sample_weights_seq = np.array([class_weights_seq[np.argmax(label)] for label in y1_batch])
        sample_weights_disease = np.array([class_weights_disease[np.argmax(label)] for label in y2_batch])

        # Combine sample weights (average)
        combined_sample_weights = np.mean([sample_weights_seq, sample_weights_disease], axis=0)

        yield X_batch, {'sequence_output': y1_batch, 'disease_output': y2_batch, 'seq_tag_output': seq_tags_batch}, combined_sample_weights

# Define a multi-output CNN model
input_layer = Input(shape=(128, 128, 1))
x = Conv2D(32, (3, 3), activation='relu')(input_layer)
x = MaxPooling2D(pool_size=(2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D(pool_size=(2, 2))(x)
x = Conv2D(128, (3, 3), activation='relu')(x)
x = MaxPooling2D(pool_size=(2, 2))(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)

# Output layers
sequence_output = Dense(len(label_mapping), activation='softmax', name='sequence_output')(x)
seq_tag_output = Dense(len(sequence_tag_mapping), activation='softmax', name='seq_tag_output')(x)
disease_output = Dense(len(disease_label_mapping), activation='softmax', name='disease_output')(x)

# Define the model
model = Model(inputs=input_layer, outputs=[sequence_output, seq_tag_output, disease_output])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss={'sequence_output': 'categorical_crossentropy',
                    'seq_tag_output': 'categorical_crossentropy',
                    'disease_output': 'categorical_crossentropy'},
              metrics={'sequence_output': 'accuracy',
                       'seq_tag_output': 'accuracy',
                       'disease_output': 'accuracy'})

# Callbacks
checkpoint = ModelCheckpoint('models/best_model.keras', monitor='val_loss', save_best_only=True)
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
history = model.fit(
    multi_output_generator(datagen, X_train, y_sequence_train, y_disease_train, seq_tags_train, class_weights_seq_dict, class_weights_disease_dict, batch_size=32),
    steps_per_epoch=len(X_train) // 32,
    epochs=20,
    validation_data=(X_val, {'sequence_output': y_sequence_val, 'seq_tag_output': seq_tags_val, 'disease_output': y_disease_val}),
    callbacks=[checkpoint, early_stopping],
    verbose=1
)

# Save the model
model_path = 'models/new_trained_multioutput_model.keras'
os.makedirs(os.path.dirname(model_path), exist_ok=True)
model.save(model_path)
print(f"Model trained and saved at {model_path}")

# Function to format predictions into hierarchical output
def format_predictions_to_hierarchy(y_pred_disease, y_pred_sequence, y_pred_seq_tag):
    results = {}

    for disease, category, seq_tag in zip(y_pred_disease, y_pred_sequence, y_pred_seq_tag):
        disease_name = disease_label_mapping_rev[disease]
        category_name = label_mapping_rev[category]
        seq_name = sequence_tag_mapping_rev[seq_tag]

        if disease_name not in results:
            results[disease_name] = {}
        if category_name not in results[disease_name]:
            results[disease_name][category_name] = []
        if seq_name not in results[disease_name][category_name]:
            results[disease_name][category_name].append(seq_name)

    return results

# Evaluate on the test set
test_loss = model.evaluate(X_test, {'sequence_output': y_sequence_test, 'seq_tag_output': seq_tags_test, 'disease_output': y_disease_test}, verbose=0)
print(f"Test loss: {test_loss}")
print(f"Sequence Loss: {test_loss[1]:.4f}")
print(f"Seq Tag Loss: {test_loss[2]:.4f}")
print(f"Disease Loss: {test_loss[3]:.4f}")

# Get predictions
y_pred = model.predict(X_test)
y_pred_sequence = np.argmax(y_pred[0], axis=1)
y_pred_seq_tag = np.argmax(y_pred[1], axis=1)
y_pred_disease = np.argmax(y_pred[2], axis=1)

# Get true labels for reports
y_true_sequence = np.argmax(y_sequence_test, axis=1)
y_true_disease = np.argmax(y_disease_test, axis=1)
y_true_seq_tag = np.argmax(seq_tags_test, axis=1)

# Format predictions
formatted_results = format_predictions_to_hierarchy(y_pred_disease, y_pred_sequence, y_pred_seq_tag)

# Print formatted output
print("Hierarchical Output:")
print(json.dumps(formatted_results, indent=4))

# Extract unique labels from y_true_seq_tag to ensure correct target names
unique_labels_seq_tag = np.unique(y_true_seq_tag)

# Filter target names based on unique labels in y_true_seq_tag
filtered_target_names_seq_tag = [
    sequence_tag_mapping_rev[idx] for idx in unique_labels_seq_tag if idx in sequence_tag_mapping_rev
]

# Ensure that target_names match the actual unique classes in the data
print("\nSequence Tag Classification Report:")
try:
    seq_tag_report = classification_report(
        y_true_seq_tag,
        y_pred_seq_tag,
        labels=unique_labels_seq_tag,  # Use unique labels for consistency
        target_names=filtered_target_names_seq_tag,  # Use matching target names
        output_dict=True
    )
    seq_tag_report_df = pd.DataFrame(seq_tag_report).transpose()
    print(seq_tag_report_df)
except ValueError as e:
    print(f"Error generating sequence tag classification report: {e}")

print("\nSequence Classification Report:")
sequence_report = classification_report(y_true_sequence, y_pred_sequence, target_names=list(label_mapping.keys()), output_dict=True)
sequence_report_df = pd.DataFrame(sequence_report).transpose()
print(sequence_report_df)

print("\nDisease Classification Report:")
disease_report = classification_report(y_true_disease, y_pred_disease, target_names=list(disease_label_mapping.keys()), output_dict=True)
disease_report_df = pd.DataFrame(disease_report).transpose()
print(disease_report_df)

# Plot training history
plt.figure(figsize=(14, 8))

plt.subplot(3, 2, 1)
plt.plot(history.history['sequence_output_accuracy'], label='Training Sequence Accuracy')
plt.plot(history.history['val_sequence_output_accuracy'], label='Validation Sequence Accuracy')
plt.title('Sequence Output Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(history.history['sequence_output_loss'], label='Training Sequence Loss')
plt.plot(history.history['val_sequence_output_loss'], label='Validation Sequence Loss')
plt.title('Sequence Output Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(history.history['seq_tag_output_accuracy'], label='Training Seq Tag Accuracy')
plt.plot(history.history['val_seq_tag_output_accuracy'], label='Validation Seq Tag Accuracy')
plt.title('Seq Tag Output Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(history.history['seq_tag_output_loss'], label='Training Seq Tag Loss')
plt.plot(history.history['val_seq_tag_output_loss'], label='Validation Seq Tag Loss')
plt.title('Seq Tag Output Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(3, 2, 5)
plt.plot(history.history['disease_output_accuracy'], label='Training Disease Accuracy')
plt.plot(history.history['val_disease_output_accuracy'], label='Validation Disease Accuracy')
plt.title('Disease Output Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(3, 2, 6)
plt.plot(history.history['disease_output_loss'], label='Training Disease Loss')
plt.plot(history.history['val_disease_output_loss'], label='Validation Disease Loss')
plt.title('Disease Output Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()

# Save mappings
with open('models/label_mapping.json', 'w') as f:
    json.dump(label_mapping, f)

with open('models/disease_label_mapping.json', 'w') as f:
    json.dump(disease_label_mapping, f)

with open('models/sequence_tag_mapping.json', 'w') as f:
    json.dump(sequence_tag_mapping, f)