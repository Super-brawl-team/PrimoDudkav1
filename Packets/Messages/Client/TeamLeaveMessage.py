from Packets.Messages.Server.TeamLeftMessage import TeamLeftMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class TeamLeaveMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        pass
        

    def process(self):
        TeamLeftMessage(self.device, self.player).Send()