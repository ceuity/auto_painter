import tensorflow as tf
from image_preprocessor import denormalize

def load_auto_painter_model():
	generator = tf.keras.models.load_model('./model/auto_painter_model.h5')

	return generator

def generate_image(model, sketch):
	pred = model(sketch[tf.newaxis,...], training=False)
	
	return denormalize(pred[0])
