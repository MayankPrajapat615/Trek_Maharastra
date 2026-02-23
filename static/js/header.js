console.log("JS loaded");

// <!-- <=======burger-menu==========> -->
const burger = document.querySelector(".burger")
const menu = document.querySelector(".menu")
const openIcon = document.querySelector(".open-icon")
const closeIcon = document.querySelector(".close-icon")

if (burger) {
  burger.addEventListener("click", (e) => {
    menu.classList.toggle("hidden");
    openIcon.classList.toggle("hidden");
    closeIcon.classList.toggle("hidden");
  });
}

document.addEventListener("click", (e) =>{
    if (!searchContainer.contains(e.target)){
        resultContainer.classList.add("hidden");
        searchContainer.classList.remove("has-results")
    }
})
// burgermenu-ends-here


// <=======search-input==========>
const input = document.getElementById("search-input")
const resultContainer = document.getElementById("results")
const searchContainer = document.querySelector(".search-container");

if (input && resultContainer && searchContainer) {
    input.addEventListener("input", async function (e) {
        const query = e.target.value.trim();

        if (query === "") {
            resultContainer.innerHTML = "";
            resultContainer.classList.add("hidden");
            searchContainer.classList.remove("has-results");
            return;
        }

        try {
            const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            renderResults(data);

        } catch (error) {
            console.error("Search error:", error);
        }
    });

    function renderResults(data) {
        resultContainer.innerHTML = "";
        currentIndex = -1;

        const { treks = [], waterfalls = [] } = data;

        if (treks.length === 0 && waterfalls.length === 0) {
            //show NO RESULTS message 
            const noResult = document.createElement("p");
            noResult.textContent = "No Result Found";
            noResult.classList.add("px-4", "py-3", "text-base", "text-bold", "text-gray-500", "text-left", "border-t");
            resultContainer.appendChild(noResult);

            resultContainer.classList.remove("hidden");
            searchContainer.classList.add("has-results");
            return
        }

        // --- TREKS SECTION ---
        if (treks.length > 0) {
            const trekTitle = document.createElement("p");
            trekTitle.textContent = "TREKS";
            trekTitle.classList.add("px-2", "mb-1", "text-sm", "font-bold", "text-secondary", "hover:bg-grey");
            resultContainer.appendChild(trekTitle);

            treks.forEach(item => {
                const li = createItem(item, "trek");
                resultContainer.appendChild(li);
            });
        }

        // --- WATERFALLS SECTION ---
        if (waterfalls.length > 0) {
            const waterfallTitle = document.createElement("p");
            waterfallTitle.textContent = "WATERFALLS";
            waterfallTitle.classList.add("px-2", "mb-1", "text-sm", "font-bold", "text-secondary");
            resultContainer.appendChild(waterfallTitle);

            waterfalls.forEach(item => {
                const li = createItem(item, "waterfall");
                resultContainer.appendChild(li);
            });
        }

        resultContainer.classList.remove("hidden");
        searchContainer.classList.add("has-results"); // 🔥 ADD THIS
    }

    function createItem(item, type) {
        const li = document.createElement("li");

        const region = item.location?.region || "";
        const district = item.location?.district || "";

        li.innerHTML = `
            <div class="flex flex-col">
                <span class="font-medium text-gray-800">${item.name}</span>
                <span class="text-xs text-gray-500">
                    ${region}${district ? " • " + district : ""}
                </span>
            </div>
        `;

        li.classList.add(
            "w-full",
            "px-3",
            "py-2",
            "hover:bg-gray-100",
            "cursor-pointer",
            "transition"
        );

        li.addEventListener("click", () => {
            if (type === "trek") {
                window.location.href = `/treks/${item.slug}`;
            } else {
                window.location.href = `/waterfalls/${item.slug}`;
            }
        });

        return li;
    }

}


let currentIndex = -1;

input.addEventListener("keydown", (e) => {
    const items = resultContainer.querySelectorAll("li");
    if (!items.length) return;

    if (e.key === "ArrowDown") {
        e.preventDefault();
        currentIndex++;
        if (currentIndex >= items.length) currentIndex = 0;
        updateHighlight(items);
    }

    else if (e.key === "ArrowUp") {
        e.preventDefault();
        currentIndex--;
        if (currentIndex < 0) currentIndex = items.length - 1;
        updateHighlight(items);
    }

    else if (e.key === "Enter") {
        const items = resultContainer.querySelectorAll("li");

        if (currentIndex >= 0 && items.length > 0) {
            e.preventDefault();   // 🔥 MUST be here
            items[currentIndex].click();
        }
    }
    console.log("KEY:", e.key);
});

input.addEventListener("input", () => {
    currentIndex = -1;
});

function updateHighlight(items) {
    items.forEach((item, index) => {
        item.classList.toggle("bg-gray-200", index === currentIndex);
    });

    if (currentIndex >= 0) {
        const activeItem = items[currentIndex];

        const containerTop = resultContainer.scrollTop;
        const containerBottom = containerTop + resultContainer.clientHeight;

        const itemTop = activeItem.offsetTop;
        const itemBottom = itemTop + activeItem.offsetHeight;

        // If item is below visible area
        if (itemBottom > containerBottom) {
            resultContainer.scrollTop = itemBottom - resultContainer.clientHeight;
        }

        // If item is above visible area
        else if (itemTop < containerTop) {
            resultContainer.scrollTop = itemTop;
        }
    }
}

//-----------------loader starts from here----------------- 

document.addEventListener('DOMContentLoaded', function () {

    const pageLoader = document.getElementById('pageLoader');

    // Hide loader using Tailwind — removes 'flex', adds 'hidden'
    function hideLoader() {
        pageLoader.classList.remove('flex');
        pageLoader.classList.add('hidden');
    }

    // Show loader using Tailwind — removes 'hidden', adds 'flex'
    function showLoader() {
        pageLoader.classList.remove('hidden');
        pageLoader.classList.add('flex');
    }

    // Hide once full page loads
    window.addEventListener('load', function () {
        hideLoader();
    });

    // Fix for back button — pageshow fires when browser restores from cache
    window.addEventListener('pageshow', function (e) {
        if (e.persisted) {
            hideLoader();
        }
    });

    const navLinks = document.querySelectorAll('a[href]:not([href="#"]):not([href^="javascript"]):not([target="_blank"])');

    navLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
            const destination = link.getAttribute('href');
            e.preventDefault();
            showLoader();

            setTimeout(function () {
                window.location.href = destination;
            }, 800);
        });
    });
});