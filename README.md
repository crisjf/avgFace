# Set-up:

1. Install opencv and scipy
```
pip install opencv-python
pip install scipy
```

2. Install dlib using homebrew (you need XCode >= 8)
```
brew cask install xquartz
brew install gtk+3 boost
brew install boost-python --with-python3
brew install dlib
pip install dlib
```

# Average faces:

1. Place all images inside a folder in images/

2. Get the face landmarks:
```
python getLandmarks.py --dir *name_of_folder*
```

3. Average the faces and save to file:
```
python faceAverage.py --dir *name_of_folder* --out *name_of_out_file*
```

# Example:

To average the faces of the presidents:
```
python getLandmarks.py --dir presidents
python faceAverage.py --dir presidents --out avg_president
```

