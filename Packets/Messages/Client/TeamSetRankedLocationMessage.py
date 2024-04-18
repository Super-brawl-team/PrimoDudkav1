
from Packets.Messages.Server.Gameroom.TeamMessage import TeamMessage
from Logic.Player import Player
from Utils.Reader import ByteStream


class TeamSetRankedLocationMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        EventSlotIndex = self.read_Vint()
        self.read_Vint()
            
    def process(self):
        TeamMessage(self.device, self.player).Send()