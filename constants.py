"""
# define all constants FOR Trikonasana
MODEL_INPUT = 99
CLASS_OUTPUT = 5
SEQUENCE_LENGTH = 5
NUMBER = '14'
ASANA = 'Trikonasana'
LABELS = ['inter1', 'inter2', 'inter3', 'trikonasana_final', 'trikonasana_start']

CSV_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Annotations/'
CSV_FILE = NUMBER + '.csv'

VIDEO_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Videos/'
VIDEO_FILE = NUMBER + '.mp4'

OUTPUT_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Output/'
OUTPUT_FILE = 'output' + NUMBER + '.csv'

MODEL_LINK = 'Models/' + ASANA + '.keras'
TF_MODEL_LINK = 'Models/' + ASANA + '.tflite'
"""

"""
# defined all the constants for Vrikshasana
MODEL_INPUT: int = 99
CLASS_OUTPUT: int = 5
SEQUENCE_LENGTH: int = 5
NUMBER = '4'
ASANA = 'Vrikshasana'
LABELS = ['inter1', 'inter2', 'inter3', 'vrikshasana_final', 'vrikshasana_start']

CSV_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Annotations/'
CSV_FILE = NUMBER + '.csv'

VIDEO_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Videos/'
VIDEO_FILE = NUMBER + '.mp4'

OUTPUT_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Output/'
OUTPUT_FILE = 'output' + NUMBER + '.csv'

MODEL_LINK = 'Models/' + ASANA + '.keras'
TF_MODEL_LINK = 'Models/' + ASANA + '.tflite'

"""

# defined all the constants for Pavana_Muktasana
MODEL_INPUT: int = 99
CLASS_OUTPUT: int = 4
SEQUENCE_LENGTH: int = 6
NUMBER = '20'
ASANA = 'Pavana_Muktasana'
LABELS = ['inter1', 'inter2', 'pavanam_final', 'pavanam_start']

CSV_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Annotations/'
CSV_FILE = NUMBER + '.csv'

VIDEO_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Videos/'
VIDEO_FILE = NUMBER + '.mp4'

OUTPUT_FILE_PATH = 'Dataset/Yoga/' + ASANA + '/Output/'
OUTPUT_FILE = 'output' + NUMBER + '.csv'

MODEL_LINK = 'Models/' + ASANA + '.keras'
TF_MODEL_LINK = 'Models/' + ASANA + '.tflite'

