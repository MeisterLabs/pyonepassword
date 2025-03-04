from ._op_item_type_registry import op_register_item_type
from ._op_items_base import OPAbstractItem


# {
#     "uuid": "zjc6s5ri3rhcxploofa67jamze",
#     "templateUuid": "003",
#     "trashed": "N",
#     "createdAt": "2021-03-19T23:27:12Z",
#     "updatedAt": "2021-03-19T23:30:10Z",
#     "changerUuid": "RAXCWKNRRNGL7I3KSZOH5ERLHI",
#     "itemVersion": 2,
#     "vaultUuid": "yhdg6ovhkjcfhn3u25cp2bnl6e",
#     "details": {
#         "notesPlain": "Note text here. **Mardown** supported.\n\nWhat does the note text look like?",
#         "passwordHistory": [],
#         "sections": [
#             {
#                 "name": "linked items",
#                 "title": "Related Items"
#             }
#         ]
#     },
#     "overview": {
#         "ainfo": "Note text here. **Mardown** supported.",
#         "ps": 0,
#         "title": "Example Secure Note"
#     }
# }


@op_register_item_type
class OPSecureNoteItem(OPAbstractItem):
    TEMPLATE_ID = "003"

    def __init__(self, item_dict):
        super().__init__(item_dict)

    @property
    def note_text(self):
        text = self.get_details_value("notesPlain")
        return text
