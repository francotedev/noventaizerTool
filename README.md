<h2>Features</h2>
<ul>
    <li>Automatically detects and processes images in a given folder.</li>
    <li>Supports 4:3 aspect ratio adjustments.</li>
    <li>Applies a pixelation effect while maintaining clarity.</li>
    <li>Enhances colors to include vibrant blues, purples, greens, oranges, and yellows.</li>
    <li>Supports both transparent PNGs and images with backgrounds.</li>
    <li>Maintains transparency for PNGs with alpha channels.</li>
</ul>

<h2>How It Works</h2>
<ol>
    <li>Provide the path to the folder containing your images.</li>
    <li>The script scans the folder for supported image formats.</li>
    <li>Each image is:
        <ul>
            <li>Cropped to 4:3 aspect ratio.</li>
            <li>Resized to apply a light pixelation effect.</li>
            <li>Enhanced with exaggerated colors and effects.</li>
            <li>If a PNG has transparency, the alpha channel is preserved.</li>
        </ul>
    </li>
    <li>Processed images are saved to an <code>output</code> subfolder inside the provided path.</li>
</ol>

<h2>Supported Formats</h2>
<ul>
    <li>PNG (<code>.png</code>)</li>
    <li>JPEG (<code>.jpg</code>, <code>.jpeg</code>)</li>
</ul>

<h2>Input</h2>
<p>Specify the full path to the folder containing the images to process.</p>

<h3>Example Input Path</h3>
<pre><code>/path/to/your/images</code></pre>

<h3>Output</h3>
<p>The processed images will be saved in:</p>
<pre><code>/path/to/your/images/output</code></pre>

<h2>Notes</h2>
<ul>
    <li>For images without transparency, the script adds vibrant backgrounds.</li>
    <li>Transparent PNGs retain their transparency after processing.</li>
</ul>

<hr>
<p><em>Maybe it's a bit late to have invented this, Franco, don't hate me... Rest in Peace (RIP) Rozu.</em></p>
