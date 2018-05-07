# -*- coding: utf-8 -*-

import face_recognition
import base64
from random import randint
import os




class ManipularImagem(object):

    # Contrutor
    def __init__(self, imagemBase64):
        self.imagemBase64 = imagemBase64
        return

    def TransformarBase64ParaImagem(self):
        image_64_decode = base64.decodestring(self.imagemBase64)
        fileName = str(randint(0, 900000000000000)) + ".jpg" #Criar um nome aleatório para o arquivo
        image_result = open(fileName, 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        return fileName

    # def TransformarImagemParaBase64(self):  # Vou usar só para teste por enquanto
    #
    #     image = open('Giovanni.jpg',
    #                  'rb')  # open binary file in read mode
    #     image_read = image.read()
    #     image_64_encode = base64.encodestring(image_read)
    #     print
    #     return image_64_encode

    def VerificarSimilaridade(self):
        fileName = self.TransformarBase64ParaImagem()
        # picture_of_me = face_recognition.load_image_file("imagens_Teste/me.jpg")
        picture_of_me = face_recognition.load_image_file(fileName)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

        unknown_picture = face_recognition.load_image_file("imagens_Teste/unknown.jpg")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if os.path.exists(fileName): #Excluir o arquivo que foi gerado
            os.remove(fileName)

        if results[0] == True:
            print("Está é uma imagem minha!")
            return "MATCH"
        else:
            print("Esta não é uma imagem minha!")
            return "NOT_MATCH"








