#Theme: Roadrip Karaoke
#Loop over the list and print everything out using for loops in two different ways 

roadrip_playlist = [
  'Bohemian Rhapsody – Queen',
  'Sweet Caroline – Neil Diamond',
  'Don’t Stop Believin’ – Journey',
  'I Wanna Dance with Somebody – Whitney Houston',
  'Mr. Brightside – The Killers',
  'Livin’ on a Prayer – Bon Jovi'
]

for i in roadrip_playlist:
  print(i)

for i in range(len(roadrip_playlist)):
  print(roadrip_playlist[i])
