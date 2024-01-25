from dataclasses import dataclass
@dataclass
class ResponseServer:

    Status : bool
    Message : str
    Data : list

    def to_dict(self):
        return {

            "Status" : self.Status,
            "Message" : self.Message,
            "Data" : self.Data
        }