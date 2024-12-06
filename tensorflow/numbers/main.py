import tkinter as tk
from PIL import Image, ImageTk
import io
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# Создание окна
root = tk.Tk()

# Создание виджета Canvas
canvas_width = 28*16
canvas_height = 28*16
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Обработчик события для рисования на Canvas
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=10)

# Привязка обработчика события к Canvas
canvas.bind("<B1-Motion>", paint)
def clear_canvas():
    canvas.delete("all")
def extract_image():
    # Получение изображения с Canvas
    postscript = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(postscript.encode('utf-8')))
    img = img.resize((28, 28))
    img = img.convert("L")
    photo_img = ImageTk.PhotoImage(img)
    # Отображение извлеченного изображения
    #tk.Label(root, image=photo_img).pack()
    
    img_array = np.array(img) 
    img_array = np.invert(img_array)
    img_array=img_array/ 255.0
    '''
    plt.figure()
    plt.imshow(img_array, cmap=plt.cm.binary)
    plt.show()
    
    '''
    img_array = np.expand_dims(img_array, axis=0)
    
    '''
    
    '''
    model = tf.keras.models.load_model('model.h5')
    #probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    prediction = model.predict(img_array)
    print(prediction)
    print(np.argmax(prediction))
# Создание кнопки для извлечения изображения
tk.Button(root, text="Extract Image", command=extract_image).pack()
tk.Button(root, text="Clear Canvas", command=clear_canvas).pack()
# Запуск главного цикла
root.mainloop()
