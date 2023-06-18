import tensorflow as tf


gpu_available = tf.config.list_physical_devices('GPU')
#is_cuda_gpu_available = tf.config.list_physical_devices('CUDA GPU')
#is_cuda_gpu_min_3 = tf.config.list_physical_devices('CUDA GPU MIN 3')

print(gpu_available)