import { motion } from 'framer-motion';
import { SparklesIcon } from './icons';

export const Overview = () => {
  return (
    <>
      <motion.div
        key="overview"
        className="max-w-3xl mx-auto md:mt-20"
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.98 }}
        transition={{ delay: 0.75 }}
      >
        <div className="rounded-xl p-6 flex flex-col gap-8 leading-relaxed text-center max-w-xl">
          <p className="flex flex-row justify-center gap-4 items-center">
            <SparklesIcon size={44} />
          </p>
          <p>
            Welcome to <strong>Chat With Guti</strong>,<br />
            a chatbot that allows you to speak directly<br />
            with <a href="https://www.linkedin.com/in/mattia-gualtieri/" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'underline' }}>Mattia Gualtieri</a>'s resume.<br />
          </p>
          <p>
            Powered by <strong>gemini-2.5-flash</strong>
          </p>
        </div>
      </motion.div>
    </>
  );
};
