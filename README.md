# RE-cycle
Automated Recyclabes Sorter built with Convolutional Neural Networks
by Tian Da Huang, Ethan Martinez, Muhammad Sajid, Miles Versaw.
<h1>Purpose</h1>
Sorting through one's recyclabes can be a tedious and daunting task, and people can become discouraged and not properly recycle their goods. This automated sorter helps individuals sort through the various kinds of recyclabes so that goods are accurately and quickly sorted.
<h1>Method</h1>
Using OpenCV and Pytorch we created a Convolutional Neural Network and image processor that can take in an image from a raspberry pi camera, detect the image, and process the image into a custom dataset. Then the image is taken through the trained neural network and analyzed.
<h1>Difficulties</h1>
The biggest difficulties arised from having to create a unique custom labeled dataset to train our Convolutional Neural Network, which was time consuming.
