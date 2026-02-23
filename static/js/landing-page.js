const searchBtn = document.getElementById("searchBtn");
const searchBox = document.getElementById("searchBox");
const searchInput = document.getElementById("searchInput");
const resultsDiv = document.getElementById("results");

// 🔍 Toggle search box
searchBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    searchBox.classList.toggle("hidden");
    searchInput.focus();
});

// ❌ Close when clicking outside
document.addEventListener("click", (e) => {
    if (!searchBox.contains(e.target) && !searchBtn.contains(e.target)) {
        searchBox.classList.add("hidden");
    }
});

// ⌨️ Search logic
let currentIndex = -1;

searchInput.addEventListener("input", async () => {
    const q = searchInput.value.trim();
    resultsDiv.innerHTML = "";

    if (!q) {
        resultsDiv.innerHTML = "";
        return;
    }

    resultsDiv.innerHTML = `
        <div class="px-3 py-2 text-sm text-gray-500">
            Searching...
        </div>
    `;
    
    currentIndex = -1;
    
    const res = await fetch(`/search?q=${encodeURIComponent(q)}`);
    const data = await res.json();
    
    resultsDiv.innerHTML = "";
    
    /* ---------- TREKS SECTION ---------- */
    if (data.treks && data.treks.length > 0) {
        const trekHeading = document.createElement("p");
        trekHeading.textContent = "TREKS";
        trekHeading.className = "text-xs font-semibold uppercase text-black px-2 mt-2 mb-1 cursor-default";
        resultsDiv.appendChild(trekHeading);
    
        data.treks.forEach(trek => {
            const item = document.createElement("a");
            item.href = `/treks/${trek.slug}`;
            item.className = "block px-3 py-2 rounded-md text-sm hover:bg-muted cursor-pointer text-black";
            item.innerHTML = `
                <div class="font-medium">${trek.name}</div>
                <div class="text-xs opacity-60">
                    ${trek.location.district}, ${trek.location.region}
                </div>
            `;
            resultsDiv.appendChild(item);
        });
    }

    /* ---------- WATERFALLS SECTION ---------- */
    if (data.waterfalls && data.waterfalls.length > 0) {
        const wfHeading = document.createElement("p");
        wfHeading.textContent = "WATERFALLS";
        wfHeading.className = "text-xs font-semibold uppercase text-black px-2 mt-3 mb-1 cursor-default";
        resultsDiv.appendChild(wfHeading);
    
        data.waterfalls.forEach(wf => {
            const item = document.createElement("a");
            item.href = `/waterfalls/${wf.slug}`;
            item.className = "block px-3 py-2 text-black rounded-md text-sm hover:bg-muted cursor-pointer";
            item.innerHTML = `
                <div class="font-medium">${wf.name}</div>
                <div class="text-xs opacity-60">
                    ${wf.location.district}, ${wf.location.region}
                </div>
            `;
            resultsDiv.appendChild(item);
        });
    }
});
    
// Enter key handling
searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        e.preventDefault();
        const items = resultsDiv.querySelectorAll("a");
    
        if (currentIndex >= 0 && items.length > 0) {
            window.location.href = items[currentIndex].href;
        } else {
            const q = searchInput.value.trim();
            if (q !== "") {
                window.location.href = `/search-page?q=${encodeURIComponent(q)}`;
            }
        }
    }
});
    

// Keyboard navigation
searchInput.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") {
        e.preventDefault();
        const items = resultsDiv.querySelectorAll("a");
        if (items.length === 0) return;
        
        currentIndex++;
        if (currentIndex >= items.length) {
            currentIndex = 0;
        }
    
        items.forEach(item => item.classList.remove("active-result"));
        items[currentIndex].classList.add("active-result");
        items[currentIndex].scrollIntoView({ block: "nearest" });
    }
    
    if (e.key === "ArrowUp") {
        e.preventDefault();
        const items = resultsDiv.querySelectorAll("a");
        if (items.length === 0) return;
        
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = items.length - 1;
        }
    
        items.forEach(item => item.classList.remove("active-result"));
        items[currentIndex].classList.add("active-result");
        items[currentIndex].scrollIntoView({ block: "nearest" });
    }
});