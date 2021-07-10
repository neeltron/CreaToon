from flask import Flask, render_template, request, make_response, redirect, url_for

def cartoonify(image):
  import cv2

  img = cv2.imread("elon.jpg")
  cv2.imwrite('input.jpg', img)

  edges = cv2.Canny(img, 100, 200)
  cv2.imwrite('canny.jpg', edges)

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_1 = cv2.medianBlur(gray, 5)
  edges = cv2.adaptiveThreshold(gray_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)
  cv2.imwrite('medianblur.jpg', edges)

  color = cv2.bilateralFilter(img, d=19, sigmaColor=200,sigmaSpace=200)
  cv2.imwrite('bilateral.jpg', color)

  cartoon = cv2.bitwise_and(color, color, mask=edges)
  cv2.imwrite('output.jpg', cartoon)



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
  return url



@app.route('/exitpoint')
def exitpoint():
  return "exit point"



if __name__ == '__main__':
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
  image = "input.jpg"
  cartoonify(image)
