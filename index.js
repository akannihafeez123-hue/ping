export default {
  async fetch(request, env) {
    if (request.method === "POST") {
      const update = await request.json();

      // Extract message text and chat ID
      const chatId = update.message?.chat?.id;
      const text = update.message?.text;

      let reply = "Hello! I am alive on Cloudflare 🚀";

      if (text) {
        if (text.toLowerCase().includes("hi")) {
          reply = "Hey there 👋, how can I help?";
        } else if (text.toLowerCase().includes("bye")) {
          reply = "Goodbye! 👋";
        } else {
          reply = `You said: ${text}`;
        }
      }

      // Send reply back to Telegram
      await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          chat_id: chatId,
          text: reply,
        }),
      });

      return new Response("OK", { status: 200 });
    }

    return new Response("Telegram Bot Worker is running!", { status: 200 });
  },
};
