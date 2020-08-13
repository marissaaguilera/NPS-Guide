"""Tests for NPS Flask app."""

import unittest
import server 


class NPSFlaskTests(unittest.TestCase):
    """Tests for my NPS site."""


# Example of tests 
# class PartyTests(unittest.TestCase):
#     """Tests for my party site."""

#     def setUp(self):
#         """Code to run before every test."""

#         self.client = server.app.test_client()
#         server.app.config['TESTING'] = True


#     def test_homepage(self):
#         """Can we reach the homepage?"""

#         result = self.client.get('/')
#         self.assertIn(b'having a party', result.data)


#     def test_no_rsvp_yet(self):
#         """Do users who haven't RSVPed see the correct view?"""

#         result = self.client.get('/')
#         self.assertIn(b'Please RSVP', result.data)


#     def test_rsvp(self):
#         """Do RSVPed users see the correct view?"""

#         rsvp_info = {'name': 'Jane', 'email': 'jane@jane.com'}

#         result = self.client.post('/rsvp', data=rsvp_info,
#                                   follow_redirects=True)

#         self.assertIn(b'Yay!', result.data)
#         self.assertIn(b'Party Details', result.data)
#         self.assertNotIn(b'Please RSVP', result.data)



#     def test_rsvp_mel(self):
#         """Can we keep Mel out?"""

#         # FIXME: write a test that mel can't invite himself
#         rsvp_info = {'name': 'Mel Melitpolski', 'email': 'mel@ubermelon.com'}

#         result = self.client.post('/rsvp', data=rsvp_info,
#                                   follow_redirects=True)

#         #self.assertIn(b'Sorry, Mel.', result.data)
#         self.assertNotIn(b'Yay!')
#         self.assertNotIn(b'Party Details', result.data)
#         self.assertIn(b'Please RSVP', result.data)




if __name__ == '__main__':
    unittest.main()