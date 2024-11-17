import random
from midiutil.MidiFile import MIDIFile
from midi2audio import FluidSynth

# Definindo a cadeia de Markov para escolher notas
notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
transition_probabilities = {
    "C4": ["D4", "E4", "G4", "A4"],
    "D4": ["E4", "F4", "A4", "C4"],
    "E4": ["F4", "G4", "B4", "C4"],
    "F4": ["G4", "A4", "D4", "E4"],
    "G4": ["A4", "B4", "E4", "F4"],
    "A4": ["B4", "C4", "G4", "D4"],
    "B4": ["C4", "D4", "F4", "A4"]
}

def generate_melody(length=20):
    melody = []
    current_note = random.choice(notes)
    for _ in range(length):
        melody.append(current_note)
        current_note = random.choice(transition_probabilities[current_note])
    return melody

# Mapeamento de notas para valores MIDI
note_to_midi = {
    "C4": 60, "D4": 62, "E4": 64, "F4": 65, "G4": 67, "A4": 69, "B4": 71
}

def create_midi(melody, filename="musica_inedita.mid"):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Track 1")
    midi.addTempo(track, time, 120)

    channel = 0
    volume = 100
    duration = 1

    for note in melody:
        midi_note = note_to_midi[note]
        midi.addNote(track, channel, midi_note, time, duration, volume)
        time += duration

    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

def midi_to_wav(midi_filename="musica_inedita.mid", wav_filename="musica_inedita.wav", soundfont_path="sforzando-v9.6.sf2"):
    fs = FluidSynth(soundfont_path)
    fs.midi_to_audio(midi_filename, wav_filename)

# Gerar melodia, salvar em MIDI e converter para WAV
melody = generate_melody(30)
create_midi(melody, "musica_inedita.mid")
midi_to_wav("musica_inedita.mid", "musica_inedita.wav", "sforzando-v9.6.sf2")

print("Música gerada e salva como 'musica_inedita.mid' e 'musica_inedita.wav'")

# pip install MIDIUtil midi2audio
# brew install fluid-synth
# https://sites.google.com/site/soundfonts4u/