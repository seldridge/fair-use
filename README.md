YouTube copyright disputes are super annoying, especially if you have a bunch of figure skating videos that trip all the filters, but are FAIR USE.

This is a simple Python script that will auto-generate a dispute response string for you.

For example, say YouTube identifies that you infringed somebody's copyright from 0m30s to 1m15s in their 7m30s long track.
Just run the included Python script:

```bash
./fair-use.py --start=00:30 --stop=01:15 --total=07:30
```

And you get the following boilerplate to fill in your copyright dispute:
```
The transformed work is a recording of an artistic and athletic performance (a figure skating routine) that uses the original work. The transformed work changes the original from a purely auditory experience to one involving a novel artistic interpretation as well as athletic demonstrations (jumps and spins). The transformed work is non-commercial in nature. The new work uses 45 seconds (10%) of the original work. This represents only a portion of the original work. The original work, being a musical recording, is designed to be listened to in its entirety. Thereby the new work, which includes the original as a recording over an ice rink sound system, does not serve as a substitute for the original. Additionally, a listener derives different, augmented enjoyment from watching the performance in the transformed work as opposed to the purely auditory experience of the original. Therefore, the market for the copyrighted, original work is unaffected by the transformed work. Thanks for taking the time to review this dispute.
```
