#!/usr/bin/env python3
        # -*- coding: utf-8 -*-
        ###Live‑Echo‑Cancellation über Mikrofon & Lautsprecher###
        import numpy as np
        import sounddevice as sd
        from lms import lms_filter

        fs = 48000
        block = 1024
        coeffs = np.zeros(block)
        mu = 5e-4

        def callback(indata, outdata, frames, time, status):
            global coeffs
            mic = indata[:, 0]
            ref = outdata[:, 0].copy()
            err, coeffs, _ = lms_filter(mic, ref, coeffs, [mu], safe=True, num_iterations=1)
            outdata[:, 0] = err

        with sd.Stream(channels=1, callback=callback, samplerate=fs, blocksize=block):
            print("Echo‑Canceller läuft … Strg‑C zum Abbrechen")
            while True:
                sd.sleep(1000)
