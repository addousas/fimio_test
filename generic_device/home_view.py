CSS_STYLE = """

"""
MENU_COMPONENT = """
  <div class="dropdown">
    <button class="dropdown-button" onclick="toggleDropdown()">
      <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
    <div class="dropdown-content" id="myDropdown">
      <a href="/">Home</a>
      <a href="/keypad">Keypad UI</a>
      <a href="/docs">API Docs</a>
    </div>
  </div>
  <script>
    function toggleDropdown() {
      document.getElementById("myDropdown").classList.toggle("show");
    }
    
    // Close the dropdown if clicked outside
    window.onclick = function(event) {
      if (!event.target.matches('.dropdown-button') && !event.target.matches('.menu-icon')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }
  </script>
"""

KEYPAD_VIEW = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phone Keypad with Recording</title>
    <style>
            body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        
        .phone {
            width: 280px;
            background-color: #e0e0e0;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .display {
            background-color: #fff;
            height: 60px;
            margin-bottom: 20px;
            border-radius: 5px;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            padding: 0 15px;
            font-size: 24px;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            position: relative;
        }
        
        .display-text {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            width: 100%;
            text-align: right;
        }
        
        .recording-indicator {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #ccc;
        }
        
        .recording-indicator.active {
            background-color: #f00;
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .keypad {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }
        
        .key {
            background-color: #fff;
            height: 60px;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            cursor: pointer;
            user-select: none;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.1s;
        }
        
        .key:active, .key.active {
            background-color: #ddd;
            transform: translateY(2px);
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        .key .subtext {
            font-size: 10px;
            position: absolute;
            margin-top: 25px;
            color: #666;
        }
        
        .controls {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 20px;
        }
        
        .control-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        
        .control-btn:hover {
            background-color: #45a049;
        }
        
        .control-btn:active {
            background-color: #3e8e41;
        }
        
        .control-btn.record {
            background-color: #f44336;
        }
        
        .control-btn.record:hover {
            background-color: #d32f2f;
        }
        
        .control-btn.record.active {
            background-color: #b71c1c;
            animation: pulse 1s infinite;
        }
        
        .control-btn.play {
            background-color: #2196F3;
        }
        
        .control-btn.play:hover {
            background-color: #1976D2;
        }
        
        .control-btn.play.active {
            background-color: #0D47A1;
        }
        
        .control-btn.clear {
            background-color: #FF9800;
        }
        
        .control-btn.clear:hover {
            background-color: #F57C00;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.7; }
            100% { opacity: 1; }
        }
        
        .control-btn:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }

            body {
      font-family: system-ui, -apple-system, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f8fafc;
      position: relative;
      flex-direction: column;
      padding-top: 5rem;
    }
    h1 {
      font-size: 10rem;
      animation: textColorAnimation 8s infinite;
    }

    h2 {
      font-size: 6rem;
      animation: textColorAnimation 6s infinite;
    }
    .space-grotesk-700 {
      font-family: "Space Grotesk", sans-serif;
      font-optical-sizing: auto;
      font-weight: <weight>;
      font-style: normal;
    }

    
    .flex-container {
        display: flex;
        flex-direction: column;
    }
    @keyframes textColorAnimation {
      0% { color: #3b82f6; }
      25% { color: #8b5cf6; }
      50% { color: #ec4899; }
      75% { color: #f59e0b; }
      100% { color: #3b82f6; }
    }
    
    @keyframes wave {
      0% { transform: rotate(0deg); }
      10% { transform: rotate(14deg); }
      20% { transform: rotate(-8deg); }
      30% { transform: rotate(14deg); }
      40% { transform: rotate(-4deg); }
      50% { transform: rotate(10deg); }
      60% { transform: rotate(0deg); }
      100% { transform: rotate(0deg); }
    }

    .wave-emoji {
      font-size: 6rem;
      animation: wave 2.5s infinite;
      transform-origin: 70% 70%;
    }
    /* Dropdown styles */
    .dropdown {
      position: absolute;
      top: 5rem;
      right: 5rem;
    }
    
    .dropdown-button {
      background-color: transparent;
      border: none;
      cursor: pointer;
      padding: 0.5rem;
      border-radius: 50%;
      transition: background-color 0.2s;
    }
    
    .dropdown-button:hover {
      background-color: rgba(0, 0, 0, 0.05);
    }
    
    .dropdown-content {
      display: none;
      position: absolute;
      right: 0;
      background-color: white;
      min-width: 160px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
      border-radius: 0.5rem;
      z-index: 1;
      animation: fadeIn 0.2s ease-out;
    }
    
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    .dropdown-content a {
      color: #333;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
      transition: background-color 0.2s;
    }
    
    .dropdown-content a:hover {
      background-color: #f1f5f9;
    }
    
    .dropdown-content.show {
      display: block;
    }
    
    /* Menu icon */
    .menu-icon {
      width: 24px;
      height: 24px;
    }
    </style>
</head>
<body>
     <div class="dropdown">
    <button class="dropdown-button" onclick="toggleDropdown()">
      <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
    <div class="dropdown-content" id="myDropdown">
      <a href="/">Home</a>
      <a href="/keypad">Keypad UI</a>
      <a href="/docs">API Docs</a>
    </div>
  </div>
  <script>
    function toggleDropdown() {
      document.getElementById("myDropdown").classList.toggle("show");
    }
    
    // Close the dropdown if clicked outside
    window.onclick = function(event) {
      if (!event.target.matches('.dropdown-button') && !event.target.matches('.menu-icon')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }
  </script>
    <div class="phone">
        <div class="display">
            <div class="recording-indicator" id="recordingIndicator"></div>
            <div class="display-text" id="display"></div>
        </div>
        <div class="keypad">
            <div id="1" class="key" data-key="1">1</div>
            <div id="2" class="key" data-key="2">2<span class="subtext">ABC</span></div>
            <div id="3" class="key" data-key="3">3<span class="subtext">DEF</span></div>
            <div id="4" class="key" data-key="4">4<span class="subtext">GHI</span></div>
            <div id="5" class="key" data-key="5">5<span class="subtext">JKL</span></div>
            <div id="6" class="key" data-key="6">6<span class="subtext">MNO</span></div>
            <div id="7" class="key" data-key="7">7<span class="subtext">PQRS</span></div>
            <div id="8" class="key" data-key="8">8<span class="subtext">TUV</span></div>
            <div id="9" class="key" data-key="9">9<span class="subtext">WXYZ</span></div>
            <div class="key" data-key="*">*</div>
            <div id="0" class="key" data-key="0">0<span class="subtext">+</span></div>
            <div class="key" data-key="#">#</div>
        </div>
        <div class="controls">
            <button class="control-btn record" id="recordBtn">Record</button>
            <button class="control-btn play" id="playBtn" disabled>Play</button>
            <button class="control-btn clear" id="clearBtn" disabled>Clear</button>
        </div>
    </div>

    <script>
        // DTMF frequencies
        const frequencies = {
            '1': [697, 1209],
            '2': [697, 1336],
            '3': [697, 1477],
            '4': [770, 1209],
            '5': [770, 1336],
            '6': [770, 1477],
            '7': [852, 1209],
            '8': [852, 1336],
            '9': [852, 1477],
            '*': [941, 1209],
            '0': [941, 1336],
            '#': [941, 1477]
        };

        // Initialize audio context
        let audioContext;
        let oscillator1;
        let oscillator2;
        let gainNode;

        // Recording variables
        let isRecording = false;
        let isPlaying = false;
        let recordedSequence = [];
        let recordStartTime;
        let currentKeyStartTime;
        let currentKey = null;

        // DOM elements
        const displayEl = document.getElementById('display');
        const recordingIndicator = document.getElementById('recordingIndicator');
        const recordBtn = document.getElementById('recordBtn');
        const playBtn = document.getElementById('playBtn');
        const clearBtn = document.getElementById('clearBtn');

        // Initialize audio context on first user interaction
        function initAudio() {
            if (!audioContext) {
                audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        // Play DTMF tone for a key
        function playTone(key) {
            if (!audioContext) initAudio();
            
            // Stop any existing tone
            stopTone();
            
            // Get frequencies for the key
            const [freq1, freq2] = frequencies[key];
            
            // Create oscillators and gain node
            oscillator1 = audioContext.createOscillator();
            oscillator2 = audioContext.createOscillator();
            gainNode = audioContext.createGain();
            
            // Set frequencies
            oscillator1.frequency.value = freq1;
            oscillator2.frequency.value = freq2;
            
            // Set gain (volume)
            gainNode.gain.value = 0.2;
            
            // Connect nodes
            oscillator1.connect(gainNode);
            oscillator2.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            // Start oscillators
            oscillator1.start();
            oscillator2.start();
            
            // Update display
            if (!isPlaying) {
                displayEl.textContent += key;
            }
            
            // Record key press if recording
            if (isRecording && !isPlaying) {
                const now = Date.now();
                
                // If there's a current key being pressed, record its duration
                if (currentKey !== null) {
                    const duration = now - currentKeyStartTime;
                    recordedSequence.push({
                        key: currentKey,
                        duration: duration,
                        pauseBefore: currentKeyStartTime - recordStartTime
                    });
                } else {
                    // First key in the sequence
                    recordStartTime = now;
                }
                
                currentKey = key;
                currentKeyStartTime = now;
            }
        }

        // Stop the tone
        function stopTone() {
            if (oscillator1) {
                oscillator1.stop();
                oscillator2.stop();
                oscillator1.disconnect();
                oscillator2.disconnect();
                gainNode.disconnect();
                
                // Record key release if recording
                if (isRecording && currentKey !== null && !isPlaying) {
                    const now = Date.now();
                    const duration = now - currentKeyStartTime;
                    recordedSequence.push({
                        key: currentKey,
                        duration: duration,
                        pauseBefore: currentKeyStartTime - recordStartTime
                    });
                    currentKey = null;
                }
            }
        }

        // Start recording
        function startRecording() {
            isRecording = true;
            recordedSequence = [];
            recordStartTime = null;
            currentKey = null;
            displayEl.textContent = '';
            recordingIndicator.classList.add('active');
            recordBtn.classList.add('active');
            recordBtn.textContent = 'Stop';
            playBtn.disabled = true;
            clearBtn.disabled = true;
        }

        // Stop recording
        function stopRecording() {
            isRecording = false;
            recordingIndicator.classList.remove('active');
            recordBtn.classList.remove('active');
            recordBtn.textContent = 'Record';
            playBtn.disabled = recordedSequence.length === 0;
            clearBtn.disabled = recordedSequence.length === 0;
        }

        // Play recorded sequence
        function playRecording() {
            if (recordedSequence.length === 0 || isPlaying) return;
            
            isPlaying = true;
            playBtn.disabled = true;
            recordBtn.disabled = true;
            clearBtn.disabled = true;
            playBtn.classList.add('active');
            displayEl.textContent = '';
            
            let currentIndex = 0;
            
            function playNextTone() {
                if (currentIndex >= recordedSequence.length) {
                    // Playback complete
                    isPlaying = false;
                    playBtn.disabled = false;
                    recordBtn.disabled = false;
                    clearBtn.disabled = false;
                    playBtn.classList.remove('active');
                    return;
                }
                
                const item = recordedSequence[currentIndex];
                
                // Highlight the key
                const keyElement = document.querySelector(`.key[data-key="${item.key}"]`);
                if (keyElement) {
                    keyElement.classList.add('active');
                    setTimeout(() => {
                        keyElement.classList.remove('active');
                    }, item.duration);
                }
                
                // Play the tone
                displayEl.textContent += item.key;
                playTone(item.key);
                setTimeout(()=> {console.log('hey')
                }, 4000);
                // Stop the tone after the recorded duration
                setTimeout(() => {
                    stopTone();
                    currentIndex++;
                    
                    // If there's another tone, schedule it
                    if (currentIndex < recordedSequence.length) {
                        const nextItem = recordedSequence[currentIndex];
                        const pauseDuration = nextItem.pauseBefore - (currentIndex > 0 ? recordedSequence[currentIndex-1].pauseBefore + recordedSequence[currentIndex-1].duration : 0);
                        
                        setTimeout(playNextTone, Math.max(0, pauseDuration));
                    } else {
                        // Playback complete
                        isPlaying = false;
                        playBtn.disabled = false;
                        recordBtn.disabled = false;
                        clearBtn.disabled = false;
                        playBtn.classList.remove('active');
                    }
                }, item.duration);
            }
            
            // Start playback
            playNextTone();
        }

        // Clear recording
        function clearRecording() {
            recordedSequence = [];
            displayEl.textContent = '';
            playBtn.disabled = true;
            clearBtn.disabled = true;
        }

        // Add event listeners to keys
        document.querySelectorAll('.key').forEach(key => {
            key.addEventListener('mousedown', () => {
                if (isPlaying) return;
                const keyValue = key.getAttribute('data-key');
                key.classList.add('active');
                playTone(keyValue);
            });
            
            key.addEventListener('mouseup', () => {
                if (isPlaying) return;
                key.classList.remove('active');
                stopTone();
            });
            
            key.addEventListener('mouseleave', () => {
                if (isPlaying) return;
                if (key.classList.contains('active')) {
                    key.classList.remove('active');
                    stopTone();
                }
            });
            
            // For touch devices
            key.addEventListener('touchstart', (e) => {
                if (isPlaying) return;
                e.preventDefault();
                const keyValue = key.getAttribute('data-key');
                key.classList.add('active');
                playTone(keyValue);
            });
            
            key.addEventListener('touchend', () => {
                if (isPlaying) return;
                key.classList.remove('active');
                stopTone();
            });
        });

        // Handle keyboard input
        document.addEventListener('keydown', (e) => {
            if (isPlaying) return;
            const key = e.key;
            if (frequencies[key] && !e.repeat) {
                const keyElement = document.querySelector(`.key[data-key="${key}"]`);
                if (keyElement) keyElement.classList.add('active');
                playTone(key);
            }
        });

        document.addEventListener('keyup', (e) => {
            if (isPlaying) return;
            const key = e.key;
            if (frequencies[key]) {
                const keyElement = document.querySelector(`.key[data-key="${key}"]`);
                if (keyElement) keyElement.classList.remove('active');
                stopTone();
            }
        });

        // Control button event listeners
        recordBtn.addEventListener('click', () => {
            if (isRecording) {
                stopRecording();
            } else {
                startRecording();
            }
        });

        playBtn.addEventListener('click', playRecording);
        clearBtn.addEventListener('click', clearRecording);
    </script>
</body>
</html>

""" 
HOME_VIEW = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raspberry Pi Landing Page</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap" rel="stylesheet">
  <style>
            body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        
        .phone {
            width: 280px;
            background-color: #e0e0e0;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .display {
            background-color: #fff;
            height: 60px;
            margin-bottom: 20px;
            border-radius: 5px;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            padding: 0 15px;
            font-size: 24px;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            position: relative;
        }
        
        .display-text {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            width: 100%;
            text-align: right;
        }
        
        .recording-indicator {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #ccc;
        }
        
        .recording-indicator.active {
            background-color: #f00;
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .keypad {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }
        
        .key {
            background-color: #fff;
            height: 60px;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            cursor: pointer;
            user-select: none;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.1s;
        }
        
        .key:active, .key.active {
            background-color: #ddd;
            transform: translateY(2px);
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        .key .subtext {
            font-size: 10px;
            position: absolute;
            margin-top: 25px;
            color: #666;
        }
        
        .controls {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 20px;
        }
        
        .control-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        
        .control-btn:hover {
            background-color: #45a049;
        }
        
        .control-btn:active {
            background-color: #3e8e41;
        }
        
        .control-btn.record {
            background-color: #f44336;
        }
        
        .control-btn.record:hover {
            background-color: #d32f2f;
        }
        
        .control-btn.record.active {
            background-color: #b71c1c;
            animation: pulse 1s infinite;
        }
        
        .control-btn.play {
            background-color: #2196F3;
        }
        
        .control-btn.play:hover {
            background-color: #1976D2;
        }
        
        .control-btn.play.active {
            background-color: #0D47A1;
        }
        
        .control-btn.clear {
            background-color: #FF9800;
        }
        
        .control-btn.clear:hover {
            background-color: #F57C00;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.7; }
            100% { opacity: 1; }
        }
        
        .control-btn:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }

            body {
      font-family: system-ui, -apple-system, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f8fafc;
      position: relative;
      flex-direction: column;
      padding-top: 5rem;
    }
    h1 {
      font-size: 10rem;
      animation: textColorAnimation 8s infinite;
    }

    h2 {
      font-size: 6rem;
      animation: textColorAnimation 6s infinite;
    }
    .space-grotesk-700 {
      font-family: "Space Grotesk", sans-serif;
      font-optical-sizing: auto;
      font-weight: <weight>;
      font-style: normal;
    }

    
    .flex-container {
        display: flex;
        flex-direction: column;
    }
    @keyframes textColorAnimation {
      0% { color: #3b82f6; }
      25% { color: #8b5cf6; }
      50% { color: #ec4899; }
      75% { color: #f59e0b; }
      100% { color: #3b82f6; }
    }
    
    @keyframes wave {
      0% { transform: rotate(0deg); }
      10% { transform: rotate(14deg); }
      20% { transform: rotate(-8deg); }
      30% { transform: rotate(14deg); }
      40% { transform: rotate(-4deg); }
      50% { transform: rotate(10deg); }
      60% { transform: rotate(0deg); }
      100% { transform: rotate(0deg); }
    }

    .wave-emoji {
      font-size: 6rem;
      animation: wave 2.5s infinite;
      transform-origin: 70% 70%;
    }
    /* Dropdown styles */
    .dropdown {
      position: absolute;
      top: 5rem;
      right: 5rem;
    }
    
    .dropdown-button {
      background-color: transparent;
      border: none;
      cursor: pointer;
      padding: 0.5rem;
      border-radius: 50%;
      transition: background-color 0.2s;
    }
    
    .dropdown-button:hover {
      background-color: rgba(0, 0, 0, 0.05);
    }
    
    .dropdown-content {
      display: none;
      position: absolute;
      right: 0;
      background-color: white;
      min-width: 160px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
      border-radius: 0.5rem;
      z-index: 1;
      animation: fadeIn 0.2s ease-out;
    }
    
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    .dropdown-content a {
      color: #333;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
      transition: background-color 0.2s;
    }
    
    .dropdown-content a:hover {
      background-color: #f1f5f9;
    }
    
    .dropdown-content.show {
      display: block;
    }
    
    /* Menu icon */
    .menu-icon {
      width: 24px;
      height: 24px;
    }
  </style>
</head>
<body>
  <div class="dropdown">
    <button class="dropdown-button" onclick="toggleDropdown()">
      <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
    <div class="dropdown-content" id="myDropdown">
      <a href="/">Home</a>
      <a href="/keypad">Keypad UI</a>
      <a href="/docs">API Docs</a>
    </div>
  </div>
  <script>
    function toggleDropdown() {
      document.getElementById("myDropdown").classList.toggle("show");
    }
    
    // Close the dropdown if clicked outside
    window.onclick = function(event) {
      if (!event.target.matches('.dropdown-button') && !event.target.matches('.menu-icon')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }
  </script>
 
  <h1 class="space-grotesk-700"> DUT</h1>
  <span class="wave-emoji">👋🏽 </span>
  <span> <strong> Date:</strong> 02-12-2025 </span>
  <span> <strong> firmware:</strong> 64131645.1554 </span>
<div style="display: flex"> 
    <svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="510.000000pt" height="200pt" viewBox="0 0 510.000000 449.000000" preserveAspectRatio="xMidYMid meet">

    <g transform="translate(0.000000,449.000000) scale(0.100000,-0.100000)" fill="#000000" stroke="none">
    <path d="M2640 4043 c-662 -51 -1315 -370 -1816 -884 -451 -464 -786 -1134 -786 -1569 1 -184 42 -299 147 -406 115 -117 250 -160 475 -151 205 8 372 60 647 201 78 40 143 71 143 67 0 -3 -23 -64 -51 -136 -96 -246 -219 -586 -219 -605 0 -64 48 -4 469 600 239 342 435 620 436 618 1 -2 -6 -64 -16 -138 -33 -246 -21 -348 46 -378 57 -26 111 -12 192 49 29 22 55 34 58 29 20 -32 113 5 156 62 l17 21 6 -21 c4 -12 14 -22 22 -22 22 0 93 48 151 103 l52 49 31 -25 c66 -56 170 -40 237 36 l33 37 14 -34 c61 -146 285 -26 375 201 l18 47 9 -34 c4 -19 8 -64 8 -100 1 -104 13 -95 143 106 10 16 12 7 12 -52 1 -102 18 -111 64 -37 40 66 92 133 104 136 4 1 10 -56 13 -127 3 -77 9 -131 15 -133 6 -2 49 53 95 122 47 69 88 125 92 125 4 0 1 -21 -7 -47 -8 -27 -15 -67 -15 -90 0 -104 107 -112 179 -12 57 78 64 190 17 274 l-23 42 141 7 c171 8 312 28 460 65 138 35 186 55 186 77 0 19 4 19 -145 -20 -204 -52 -335 -69 -540 -69 -104 0 -222 3 -260 7 -59 7 -73 5 -84 -8 -21 -25 -5 -34 79 -41 88 -8 119 -24 147 -78 38 -74 35 -159 -10 -224 -26 -39 -70 -65 -92 -57 -14 6 -16 15 -11 58 18 139 19 171 1 186 -10 9 -19 10 -23 4 -4 -6 -43 -63 -87 -128 l-80 -118 -3 126 c-2 113 -4 126 -20 126 -20 0 -61 -40 -116 -113 -41 -56 -44 -53 -48 53 -2 60 -6 75 -20 78 -10 2 -19 -6 -23 -20 -13 -41 -88 -188 -97 -188 -4 0 -8 15 -8 33 0 35 -23 122 -39 146 -14 22 -35 0 -51 -51 -36 -121 -126 -250 -202 -289 -98 -50 -159 13 -128 134 18 70 17 185 -3 222 -21 42 -65 81 -112 101 -45 19 -256 32 -525 34 -85 0 -160 4 -167 8 -8 5 3 27 38 72 28 36 54 71 58 78 5 10 57 18 167 27 385 33 536 38 1164 41 622 3 655 4 655 21 0 13 -11 20 -40 25 -22 4 -260 8 -530 9 -482 1 -773 -8 -1130 -37 -99 -7 -193 -14 -208 -14 l-28 0 50 74 c115 170 259 452 318 624 20 59 28 102 31 182 4 100 2 107 -25 160 -18 34 -45 66 -72 85 -37 26 -51 30 -109 30 -50 -1 -78 -7 -112 -24 -57 -30 -154 -128 -209 -211 -43 -67 -287 -548 -423 -837 -67 -141 -80 -163 -100 -163 -26 0 -401 -58 -591 -91 -118 -20 -128 -24 -125 -43 3 -20 11 -21 168 -27 91 -3 238 -7 328 -8 89 0 162 -5 162 -9 0 -5 -26 -69 -59 -143 -32 -74 -89 -206 -125 -295 l-67 -160 -87 -52 c-508 -300 -951 -348 -1176 -128 -132 128 -173 328 -121 578 40 190 162 492 287 710 148 258 283 434 503 654 174 174 268 253 445 373 730 494 1646 621 2249 311 313 -161 513 -463 528 -800 6 -122 -1 -176 -39 -292 -22 -69 -18 -99 8 -63 47 64 79 268 64 409 -25 234 -118 427 -289 596 -92 92 -163 143 -280 202 -239 120 -598 178 -941 151z m82 -708 c89 -61 106 -192 47 -370 -58 -175 -273 -580 -369 -695 l-25 -30 -230 -26 c-126 -13 -236 -27 -244 -29 -23 -9 -7 30 119 294 265 555 342 692 444 789 97 92 187 115 258 67z m-388 -1157 c-4 -7 -33 -44 -63 -82 l-56 -69 -193 6 c-107 3 -196 8 -198 10 -2 2 4 22 12 45 19 48 -5 42 301 77 109 13 199 24 201 24 2 1 0 -5 -4 -11z m-551 -98 l-16 -40 -86 1 c-47 1 -140 4 -206 8 l-120 6 140 23 c233 37 249 40 277 41 l26 1 -15 -40z m380 -96 c10 -10 -118 -148 -238 -257 -131 -118 -348 -284 -353 -269 -1 5 47 127 108 271 l112 261 182 0 c101 0 186 -3 189 -6z m553 -13 c206 -7 224 -9 270 -32 67 -33 94 -76 94 -151 0 -115 -58 -225 -137 -260 -36 -16 -50 -17 -77 -8 -19 6 -41 19 -51 30 -17 19 -16 23 19 94 39 79 40 96 2 96 -38 0 -78 -52 -84 -110 -4 -47 -9 -54 -73 -115 -67 -63 -99 -80 -99 -51 0 8 9 44 20 80 21 68 20 86 -6 86 -8 0 -14 7 -14 15 0 19 -33 19 -69 0 -46 -23 -109 -103 -132 -166 -17 -45 -33 -69 -73 -102 -91 -78 -146 -95 -182 -56 -29 33 -29 130 1 354 l27 199 45 53 45 53 127 -1 c69 0 225 -4 347 -8z m-943 -543 c-82 -117 -220 -316 -307 -443 -87 -126 -163 -234 -168 -240 -14 -16 192 537 223 596 4 9 43 40 86 69 94 65 214 155 268 203 22 19 42 34 43 32 2 -2 -63 -99 -145 -217z m753 77 c-34 -70 -85 -125 -114 -125 -19 0 -15 7 53 91 36 45 71 89 78 99 6 11 13 17 16 15 2 -3 -13 -39 -33 -80z"/>
    </g>
    </svg>

</div>

</body>
</html>
"""