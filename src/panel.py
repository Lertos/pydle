
class Panel:
    
    COLOR_NO_PADDING = (74, 22, 10)
    COLOR_WITH_PADDING = (22, 74, 10)
    
    WHITE = (255, 255, 255)
    
    TEXT_ALIGN_LEFT = 0
    TEXT_ALIGN_RIGHT = 1
    TEXT_ALIGN_CENTER = 2
    
    
    def __init__(self, pygame, window, font, debug, width, height, borderColor, posX, posY, paddingX, paddingY):
        self.pygame = pygame
        self.window = window
        self.font = font
        
        self.spaceWidth = font.size(' ')[0]
        self.fontHeight = font.size('Tg')[1]
        
        self.debug = debug
        self.drawBorder = True
        
        self.textToDraw = ''
        
        self.width, self.height = width, height
        
        self.borderColor = borderColor
        
        self.posX, self.posY = posX, posY
        self.paddingX, self.paddingY = paddingX, paddingY
        
        self.rect = self.pygame.Rect((posX + paddingX, posY + paddingY), (self.width - (paddingX*2), self.height - (paddingY*2)))
        
        
    def drawPanel(self):
        if self.debug:
            self.drawDebug()
            
        if self.drawBorder:
            self.drawSquare(self.borderColor, 1, self.posX, self.posY, self.width, self.height)
        
        self.drawText(self.rect)


    def drawDebug(self):
        self.drawSquare(self.COLOR_NO_PADDING, 0, self.posX, self.posY, self.width, self.height)
        self.drawSquare(self.COLOR_WITH_PADDING, 0, self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        
        
    def drawSquare(self, color, borderWidth, posX, posY, width, height):
        rect = self.pygame.Rect(posX, posY, width, height)
        self.pygame.draw.rect(self.window, color, rect, borderWidth, border_radius=1)


    def setTextToDraw(self, text):
        self.textToDraw = text


    def drawText(self, rect, align=TEXT_ALIGN_LEFT):
        lineLengths, lineImages = self.getImagesAndLengthFromText(self.textToDraw, rect[2])
        
        lineBottom = rect[1]
        lastLine = 0

        for length, images in zip(lineLengths, lineImages):
            #If a new line is desired, skip a line
            if length == -2:
                lastLine += 1
                lineBottom += self.fontHeight - 2
            #If there are images, then draw them 
            elif length != -1:
                lineLeft = rect[0]
                if align == self.TEXT_ALIGN_RIGHT:
                    lineLeft += + rect[2] - length - self.spaceWidth * (len(images)-1)
                elif align == self.TEXT_ALIGN_CENTER:
                    lineLeft += (rect[2] - length - self.spaceWidth * (len(images)-1)) // 2
                    
                if lineBottom + self.fontHeight > rect[1] + rect[3]:
                    break
            
                for i, image in enumerate(images):
                    x, y = lineLeft + i * self.spaceWidth, lineBottom
                    self.window.blit(image, (round(x), y))
                    lineLeft += image.get_width()
            
                lastLine += 1
                lineBottom += self.fontHeight + 2


    def getImagesAndLengthFromText(self, textList, maxLineLen):
        lineLengths = [0]
        lineImages = [[]]

        for line in textList:
            sections = line.split('::')
            color = (self.WHITE)

            for i in range(0, len(sections)):
                #If section is simply a line break
                if sections[i] == '':
                    lineLengths.append(-1)
                    lineImages.append([-1])
                    continue
                
                #If section is a empty line
                if sections[i] == '\n':
                    lineLengths.append(-2)
                    lineImages.append([-2])
                    continue
                
                #If section is the color
                if i%2 == 0:
                    color = self.getColorFromCode(sections[i])
                    continue
                
                #If section is the actual text
                wordList = sections[i].split(' ')
                imageList = [self.font.render(word, True, color) for word in wordList]
                
                for image in imageList:
                    width = image.get_width()
                    lineLen = lineLengths[-1] + len(lineImages[-1]) * self.spaceWidth + width
                    
                    if lineLengths[-1] == -1:
                        lineLengths.append(0)
                        lineImages.append([])
                    
                    if len(lineImages[-1]) == 0 or lineLen <= maxLineLen:
                        lineLengths[-1] += width
                        lineImages[-1].append(image)
                    else:
                        lineLengths.append(width)
                        lineImages.append([image])

        return lineLengths, lineImages

    
    def getColorFromCode(self, code):
        if code == 'red':
            return (245, 66, 66)
        elif code == 'green':
            return (66, 245, 72)
        elif code == 'yellow':
            return (245, 239, 66)
        else:
            return (250, 250, 250)
            
        