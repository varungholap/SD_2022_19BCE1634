class Piece1:
    def __init__(self, name, player, position, steps):
        self.name = name
        self.player = player
        self.currentPosition = position
        self.oldPosition = position
        self.newPosition = None
        self.steps = steps
        self.alive = True

    def prepareMove(self, move):
        self.predictMove(move)

    def move(self):
        pass

    def isValidMove(self, move):
        pass

    def predictMove(self, move):
        pass

    def getNewPosition(self):
        return self.newPosition

    def getOldPosition(self):
        return self.oldPosition

    def getCurrentPosition(self):
        return self.currentPosition

    def getName(self):
        return self.name

    def getPlayer(self):
        return self.player

    def isAlive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def killPiece(self, piece, board):
        if self.isEnemy(piece):
            piece.kill()
            if piece.belongsToPlayer1():
                board.removedPlayer1Piece()
            else:
                board.removedPlayer2Piece()

    def isEnemy(self, piece):
        return not piece.player == self.player

    def belongsToPlayer1(self):
        return self.player == 1

    def belongsToPlayer2(self):
        return self.player == 2

    def moveLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        position.updateCol(self.getStepsToMove(moveColFactor))

    def moveRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        position.updateCol(self.getStepsToMove(moveColFactor))

    def moveForward(self, position):
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updateRow(self.getStepsToMove(moveRowFactor))

    def moveBackward(self, position):
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updateRow(self.getStepsToMove(moveRowFactor))

    def moveFrontLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updatePosition(self.getStepsToMove(moveRowFactor), self.getStepsToMove(moveColFactor))

    def moveFrontRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updatePosition(self.getStepsToMove(moveRowFactor), self.getStepsToMove(moveColFactor))

    def moveBackLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updatePosition(self.getStepsToMove(moveRowFactor), self.getStepsToMove(moveColFactor))

    def moveBackRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updatePosition(self.getStepsToMove(moveRowFactor), self.getStepsToMove(moveColFactor))

    def getStepsToMove(self, factor):
        return factor * self.steps
