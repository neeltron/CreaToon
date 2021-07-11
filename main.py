from flask import Flask, render_template, request, make_response, redirect, url_for
import cv2
import numpy as np
import urllib.request
from PIL import Image
import requests
from io import BytesIO

def url_to_image(url):
  resp = requests.get('https://firebasestorage.googleapis.com/v0/b/creatoon-40449.appspot.com/o/Images%2F1625958983257?alt=media&token=36b36e83-7942-46e3-ad9d-52b498eef698')
  img = Image.open(BytesIO(resp.content))
  img.save('input.jpg')
  return img



def cartoonify(image):
  url_to_image(image)
  img = cv2.imread('input.jpg')
  edges = cv2.Canny(img, 100, 200)
  cv2.imwrite('canny.jpg', edges)

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_1 = cv2.medianBlur(gray, 5)
  edges = cv2.adaptiveThreshold(gray_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)
  cv2.imwrite('medianblur.jpg', edges)

  color = cv2.bilateralFilter(img, d=19, sigmaColor=200,sigmaSpace=200)
  cv2.imwrite('bilateral.jpg', color)

  cartoon = cv2.bitwise_and(color, color, mask=edges)
  cv2.imwrite('static/output.jpg', cartoon)



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def index():
  return "Hello World"



@app.route('/entrypoint', methods = ['GET', 'POST'])
def entrypoint():
  url = request.args.get('img')
  cartoonify(url)
  return url



@app.route('/exitpoint')
def exitpoint():
  return "https://CreaToon.neeltron.repl.co/static/output.jpg"



if __name__ == '__main__':
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
  image = "input.jpg"
  cartoonify(image)
